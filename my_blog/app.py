# from flask import Flask, render_template, abort
# import os
# import markdown


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# POSTS_DIR = os.path.join(BASE_DIR, "posts")
# TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
# STATIC_DIR = os.path.join(BASE_DIR, "static")

# app = Flask( __name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR )


# # Load posts from the "posts" folder
# def load_posts():
#     posts = []
#     for filename in os.listdir(POSTS_DIR):
#         if filename.endswith(".md"):
#             path = os.path.join(POSTS_DIR, filename)
#             with open(path, "r", encoding="utf-8") as f:
#                 # convert markdown to HTML here
#                 content = f.read() 
#                 # html = markdown.markdown(content) 
#                 html = markdown.markdown(content, extensions=["fenced_code", "codehilite", "extra"])
#                 slug = filename[:-3] # remove .md 
#                 posts.append({"slug": slug, "content": html, "title": slug.replace("_", " ").title()})
#                 # posts.reverse()
#     return posts


# @app.route("/")
# def index():
#     posts = load_posts()
#     return render_template("index.html", posts=posts)


# @app.route("/post/<slug>")
# def post(slug):
#     posts = load_posts()
#     for p in posts:
#         if p["slug"] == slug:
#             return render_template("post.html", post=p)
#     abort(404)


# @app.route("/test-paths")
# def test_paths():
#     return f"""
#     BASE_DIR: {BASE_DIR}<br>
#     POSTS_DIR exists: {os.path.exists(POSTS_DIR)}<br>
#     TEMPLATES_DIR exists: {os.path.exists(TEMPLATES_DIR)}<br>
#     STATIC_DIR exists: {os.path.exists(STATIC_DIR)}<br>
#     """


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, abort
import os
import markdown
import frontmatter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "posts")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

def load_posts():
    posts_list = []
    # Get filenames and sort them alphabetically
    # Since they start with YYYY-MM-DD-HHMM, alphabetical = chronological
    filenames = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    filenames.sort(reverse=True) # Newest (highest year/month) first

    for filename in filenames:
        path = os.path.join(POSTS_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            # content = f.read()

            # This parses the "---" block and the content separately
            post_data = frontmatter.load(path)

            html = markdown.markdown(post_data.content, extensions=["fenced_code", "codehilite", "extra", "pymdownx.tasklist"])

            # Use the filename as the slug
            slug = filename[:-3] 
            
            # Clean up the title:
            # 1. Remove the date (first 15 chars: "YYYY-MM-DD-HHMM")
            # 2. Replace underscores/hyphens with spaces
            # 3. Capitalize
            display_title = slug[15:].replace("-", " ").replace("_", " ").title()
            
            # Extract the date for display on the page
            post_date = slug[:10] 

            # Get time
            post_time = slug[11:15]

            posts_list.append({
                "slug": slug, 
                "content": html, 
                "title": display_title,
                "date": post_date,
                # "time": post_time,
                "time": post_data.get("time", "--"),
                "tags": post_data.get("tags", []) # Returns a list of tags
            })
            
    return posts_list

# --- CACHE INITIALIZATION ---
# This runs once when the server starts
ALL_POSTS = load_posts()
# Create a dictionary for instant lookups by slug
POSTS_DICT = {p["slug"]: p for p in ALL_POSTS}

@app.route("/")
def index():
    # Fast: just returns the list already in memory
    return render_template("index.html", posts=ALL_POSTS)

@app.route("/post/<slug>")
def post(slug):
    # Fast: instant dictionary lookup
    p = POSTS_DICT.get(slug)
    if p:
        return render_template("post.html", post=p)
    abort(404)


@app.route("/tag/<tag_name>")
def tag_page(tag_name):
    # Filter posts that contain the specific tag
    # We use .lower() to make the search case-insensitive
    filtered_posts = [p for p in ALL_POSTS if tag_name.lower() in [t.lower() for t in p['tags']]]
    
    if not filtered_posts:
        abort(404)
        
    return render_template("index.html", posts=filtered_posts, tag_filter=tag_name)


@app.route('/about')
def about():
    # Path to your about.md file
    # path = "about.md" 
    filename = "2026-01-26-1608-about-me.md"
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
                post_data = frontmatter.load(path)
                content = markdown.markdown(post_data.content, extensions=["fenced_code", "codehilite", "extra"])
        
                # content = markdown.markdown(post.content, extensions=["fenced_code", "codehilite", "extra"])
                return render_template('post.html', post={
                    'title': post_data.get('title', 'About Me'),
                    'content': content
                })
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)