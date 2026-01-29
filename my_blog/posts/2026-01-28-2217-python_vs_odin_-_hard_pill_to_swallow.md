---
title: Python vs Odin - Hard Pill to Swallow
date: 2026-01-28 22:17
time: 10:17 PM
tags: [python, odin, programming]
---


## Python vs Odin - Hard Pill to Swallow

I've been thinking a lot about the time that I've spent studying Odin. Recently, I abruptly had to solve a problem -- and I didn't even think about using Odin. Like, Odin never crossed my mind until well after the work was done. This language, that I say I love and use every day for personal projects, when the rubber hit the road - I didn't even consider it. This shocked me and forced me to address why this happened. This is because the task was to build a content API with json values, and that was very straightforward to do - both to build and deploy - in Python. It made me wonder why I was spending so much time in Odin -- and what I can learn from this experience. 

 

For the past couple years I've been using Odin and Python daily. To me, I was trying to reach a place where solving a task in one language meant solving it in another. I wanted to be able to reach for either in case I needed to solve a problem. The goal was to be "fluent" in both. And while I have made great strides (I regularly solve Leetcode in both, I make small home applications in both), I think that my initial goal was a bit misguided. I have had to, regardless of how it makes me feel, come to the following conclusion:

 
##
### If you're using Odin to solve problems that can be solved in Python, you're missing the point. 
##
 

Odin (for problems Python can solve), in every way, is a less capable Python. It has fewer libraries. It has a smaller ecosystem. It's less flexible and thus more annoying to use (for example, as soon as you have a list of lists ... forget about it - just use Python). Once you're comfortable with manual memory management and pointers (which Odin makes very clear and ergonomic), you're left with the raw reality of how useful each language is. And more and more, solving problems (and building applications) in both languages showed me that Odin is just a slower, more arduous way to get to the same place. I've had to come to the place where I accept (and understand) that Python is not only a great language, but a profoundly useful tool. 

 

Much of the reason that I was learning a compiled language (I tried a bunch: Rust, Zig, C++, etc. -- none of them stuck until Odin) is because of the insecurities I had with Python's performance. Let me be clear: I never had a problem with Python's performance, but so many people online had a problem with Python's performance, that I considered it foolish not to address this issue that I would undoubtedly come to sometime in my Python career. I also was scared of manual memory management and (try as I might) not fully comfortable with pointers. How could I consider myself a programmer if I didn't understand that stuff? (Even though I was still making projects and having a grand old time building things and solving problems, the lack of understanding in this area made me quite insecure). I mean, how can you be a programmer if you don't understand pointers, right? ... right?

 

Let me share a scenario with you, and let me know if you've encountered something similar. You're building something in Python (or your preferred dynamic language of choice) and someone that you respect says something like "You're gonna hit a performance wall at some point. When that happens, you're going to have to dive into C." Which then begs the obvious question: If I have to have an "escape hatch" to C, why don't I just write this in C to begin with? It seems like an obvious question, but it reveals an underlying assumption and misunderstanding: the idea that somehow - somewhere out there - is a "best" language, and if I just write it in that language, I won't have to deal with problems like this from now on. It's coming from a sincere place and a genuine desire to do what is best. (You know: think ahead, plan for the future - all that good stuff.) However, it misses the reality that at the end of the day a language is just a tool. That's it. No more. No less. Is a saw better than a screwdriver? Is a hammer better than a pliers? Depends -- what are you trying to do? You can cut trough a 4" by 4" piece of wood with an exacto knife, but a saw would be a far more practical choice. You can screw in a screw with the back end of a hammer (which is called a claw, btw) but a screwdriver would be far less work and take far less time.

##
### A language is just a tool
## 

So, with this understanding -- that a language is just a tool -- it begs another question: what problem are you solving, and what is the best tool for that situation? A part of that is based on preference (do you like the syntax, do you enjoy writing it, is the language fun to write and fun to read, etc.), but a large part of that decision is the practicality of the language: Is this the "best tool for the job"? And let me be clear: when I say that, I mean: Does this language excel in solving the problem that you're asking it to solve? Not can it solve it (like an exacto knife cutting through a 4" by 4" piece of wood), but does it excel in doing it? (like a saw for that block of wood. Or better yet an electrical tool, like a circular saw, or a miter saw or something like this) You see? That's what I mean.

 

The "brick and wall" analogy really cleared things up for me: Odin is really good at making small, high-performance bricks. Most of the time, however, I'm trying to build walls. Or houses. Or groups of houses. You see what I mean? So, I find Python to be a far better tool for what I'm trying to do. So, are you trying to make a brick, or are you trying to make a house?

 

So, again I say: Solving problems in Odin that can be solved in Python is missing the point. Use Python where Python excels and use Odin where Odin excels. Python's vast libraries, infrastructure, ecosystem and communities make it hands-down the most ergonomic and practical solution for many programming related problems. Not all (because no single language handles all problems).

 

Do you need the control that a compiled, C-style language provides? Odin is an excellent choice. In what areas does Odin shine? Game engines, tools that require predictable low-latency (like real-time stock trading), embedded systems (small footprint, no heavy runtime), performance-critical sections of code, stuff like that.

 

A winning combination (crazily enough) is exactly what the programmer that you respected suggested at the very beginning: Use Python to solve the big sweeping problems (the circular saw) and then "dive into C" (or Odin) to solve specific, performance-critical situations (the exacto knife) if necessary (btw, libraries like numpy make this "two language approach" less and less necessary. Since it's optimized c/fortran code, it's reaching the theoretical limit of how fast math computations can be done IN ANY LANGUAGE. It uses MKL or OpenBLAS, which is the fastest math humans have written in the last 40 years. LOL). That way you have both: the practical speed and ergonomics of a language as established as Python, combined with the fine-tuned precision and control that a language like C (Odin) provides. And you're using both in ways the languages excel.

 

It's wild to spend years learning something and then finally come back to, "Yeah, I guess that guy was right."


Mike C

