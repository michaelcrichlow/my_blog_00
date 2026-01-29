---
title: The Profound Difference Between Python and Odin
date: 2026-01-28 21:56
time: 9:56 PM
tags: [odin, python, programming]
---


## The Profound Difference Between Python and Odin

I tentatively started exploring Odin (since I didn't have access to Jai) and since then has become by go-to language for recreational programming. I truly love using it. I like the fact Odin feels elegant, simple, as fast as C and in many ways as ergonomic as Python. I've often heard the term "Use the right tool for the job" but understand that at a deeper level now.

As I was programming last night, a problem I was given was to write a function 'flatten()' that flattens a nested list. Simply:

Example:  
```
Input: [1, [2, 3], [4, [5]]] → Output: [1, 2, 3, 4, 5]
```

Doing this in Odin is... a pain. Now, I don't know if there's another way to do it, but the way I ended up doing it involved reflection, pointer arithmetic and throwing away the compiler safety of types completely, because Odin is a statically typed language. As such, you can't have elements of different types in the same array (or slice) - it won't compile.

```python
# Odin Code
my_array := []int{1, {2, 3}}   # <-- Won't Compile. Contains both 'ints' and 'slice of ints'. 
```

So, I used 'any' to get the job done (which immediately makes things a whole lot more complicated). There are things I tend to stay away from in Odin (scary stuff!) and 'any' is one of them. Included in that list are 'transmute()', pointer arithmetic, reflection and anything so low-level it feels if anything goes wrong the computer will just blow up. >_<


I don't want to post the code here, though it's here if you want to see it [here]( https://github.com/michaelcrichlow/2026_01_07---flatten-with-Odin-and-Python/tree/main ). Suffice it to say, doing ```flatten()``` in Python is WAAAAAAAAAYYYYYYYYY easier than in Odin. It really shows, "Hey, if you have nested lists, just do it in Python, solve the problem and move on with your life." :lol: There are things that Odin does well, and acting like a dynamic language is not one of those things.


That's it for now. Much love, y'all!

Mike C

