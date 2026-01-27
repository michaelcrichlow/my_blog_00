import os
from pygments.formatters import HtmlFormatter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Make sure the static folder exists
os.makedirs(STATIC_DIR, exist_ok=True)

style = "default"  # try "monokai", "friendly", "colorful", etc.
css = HtmlFormatter(style=style).get_style_defs('.codehilite')

css_path = os.path.join(STATIC_DIR, "code.css")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print(f"CSS written to {css_path}")
