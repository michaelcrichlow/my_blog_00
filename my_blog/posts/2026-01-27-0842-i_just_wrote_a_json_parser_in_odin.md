---
title: Testing Markdown
date: 2026-01-27 08:43
time: 8:43 AM
tags: [odin, programming, json, parser]
---


## I just wrote a JSON parser in Odin!

In the endless pursuit to become a better programmer (and hopefully be paid for my expertise in the future), I'm always on the hunt for ways to improve. What projects do I build? What books should I read? Stuff like that. Well, I've seen more than one person recommend that a project every developer should do - both for the sake of learning and experience - is build a JSON parser. So, I did just that.


It took a few days to do, and well -- it was a lot. First of all, I was following a blog post called "Writing a simple JSON parser" by Phil Eaton. The example code was implemented in Python, but since Odin has been my language of choice lately, I chose to build it in that language. The first thing you realize is that there's a lot of "Here's where we want to end up at the end" kind of thinking, which I thought was really cool. It sets up expectations and gives a clear endpoint/goal. It also showed the realities of what I would have to build in Odin in regard to tooling/ergonomics. 


For example, in Python to test if two dictionaries are equal, you'd simply do:

```python
if a == b:
```


That's it. That's the entire code. However, in Odin, simple comparisons like that only exist for basic types (int, float, string, bool, none). Anything beyond that and you have to build the functionality yourself. So, before I even got to building the JSON parser, I had to build the ability to *test* my parser, which meant I had to make an ergonomic way to test equality. I ended up going with the name "deep_equal()" as an overloaded function, into which I built the functionality of each type necessary. Then the checks would dive recursively as necessary to end up at the simple comparison types and then do the checks from there. So, my Odin code to test to maps, slices, etc. would look like this:

```python
if deep_equal(a, b) {}
```


That's pretty much as ergonomic as Python, and once it was built it was straightforward to use. Very cool! Any now I have a "deep_equal()" function that I can use for anything that needs to check equality in the future (and the knowledge on how to expand functionality as necessary). 👍


There's so much more to say, but I don't want to write too much more for now. If you'd like to check out my code, you can do so here: [Odin Code](https://github.com/michaelcrichlow/2026_01_05---Simple-JSON-parser-written-in-Odin/blob/main/tests_01.odin)


Much love, y'all! Hope 2026 is going to better for all of us (regardless of what happens in the world, we're gonna keep going). Cheers! 😊


Mike C

