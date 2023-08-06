---
layout: post
title: "Useful research / programming / productivity tools"
---


## Research Tools

1. [Obsidian](https://obsidian.md/)

I'm a terrible notetaker. Like really, really bad. I've been slowly trying to be more diligent about storing little experimental results (e.g. power simulations or theoretical expectations). I've tried a decent number of different note-taking apps over the years and it seems like Obsidian has two elements 




2. [Paperpile](https://paperpile.com/app)

Managing citations and a bibliography can be quite daunting when developing a project proposal 


3. 



## Programming Tools

I've been programming for a little while now but I hadn't really thought that hard about the tools that I've used in order to code more efficiently or to understand my habits. This section mainly emerged from me trying to think about the libraries and tooltips that I enjoy using the most and that have improved my research substantially over the past couple of years. Most of the tools boil down to (my own) two goals of programming: (1) be as lazy as possible and (2) be as correct as possible.

1. [hypothesis](https://hypothesis.readthedocs.io/en/latest/) (or [property-based testing](https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237) more generally)

This is more of a thematic pointer rather than a library per-say but when writing numerical algorithms, we often want to test specific functions (e.g. likelihoods) against a wide range of input parameters. I still probably don't write tests as much as I probably should but relying on smart software to evaluate bugs when dealing with extreme parameter choices is very useful for locking down and testing core functions to make sure that you have guaranteed behavior. 

The first library I encountered for this was the excellent [hypothesis](https://hypothesis.readthedocs.io/en/latest/) library for Python. The abiity to simply set ranges for inputs and handling of different types is really quite amazing to completely battle-test numerical code. It doesn't work as well for more nuanced object-oriented testing - base `pytest` can still be really great there - but works like a dream for more numerical functions. I would definitely recommend using this library to validate your functions against well-constructed inputs for finding trickier edge-cases.

These sorts of "checks against specs" are a much more common framing in functional programming languages where you have strongly defined types and notions of correctness. It just so happens that much of research code in modern biology is written in more dynamically typed languages (e.g. `python`), but applying these tools can be equally fruitful in this setting and worth adding to your toolkit.   

2. [`pre-commit`](https://pre-commit.com/)

In computational biology it is perhaps less common to care a lot about code style or interpretabilty, but using something like [`pre-commit`](https://pre-commit.com/) can allow you to ensure that your code is readable and interpretable [^1] It also very nicely just automatically reduces variability in styles to a recognized standard across languages which is great! 

Some clear benefits of using these tools are: 

* Can instantly make your code easier to read
* Makes it easier to collaborate on coding projects since you have agreed standards on style
* Can ensure robust documentation and sufficient commenting for reproduceability

In many ways this gets to the "lazy" programmer aspect since `pre-commit` will be quite direct in what you need to fix in your code or documentation, rather than you having to come to that realization in 2-5 days or so. You can also customize your experience quite a lot here. 

Once you set this up (even for one-off-scripts), it takes maybe 1-2 months before you automatically start to adopt the style guidelines and have to rely on it much less. I would definitely recommend this tool for researchers who want to ply their craft in an industry setting as well since you might be working on more shared products and this can be useful for building your coding habits more diligently. 


## Productivity Tools 



[1]: There are lots of researchers who care a lot about this - but generally speaking with the frequency at which analyses are required, style and interpretability frequently can take a backseat.