---
layout: post
title: "Useful research / programming / productivity tools"
---

## Research Tools

### [Obsidian](https://obsidian.md/)

I'm a terrible notetaker. Like really, really bad. I've been slowly trying to be more diligent about storing little experimental results (e.g. power simulations or theoretical expectations). I've tried a decent number of different note-taking apps over the years and it seems like Obsidian has two elements that put it much farther ahead for note-management than other tools: 

* Its usage of simple markdown language
* Its based on plain-text stored in a directory 

The first point means that writing small equations or linking in images is quite straightforward. The second means that if you combine it with something like Dropbox or another storage platform that you can very easily have your notes be transferrable on a different machine.

### [Paperpile](https://paperpile.com/app)

Managing citations and a bibliography can be quite daunting when developing a grant / paper. In biology (and modern science more generally) the pace of papers coming out that are relevant to your project increases at a fast rate. I've been using Paperpile since around 2020 and its been the one tool that I really think the paid version has massive benefits. 

Honestly, the ability to directly "search + cite" in google docs and easy exportation to BibTeX make this a gamechanger. There are some features related to shared libraries that can be quite annoying to deal with (e.g. syncing to Overleaf) but they are improving this substantially year by year so it might hit even greater heights. 

## Programming Tools

I've been programming for a little while now but I hadn't really thought that hard about the tools that I've used in order to code more efficiently or to understand my habits. This section mainly emerged from me trying to think about the libraries and tooltips that I enjoy using the most and that have improved my research substantially over the past couple of years. Most of the tools boil down to (my own) two goals of programming: (1) be as lazy as possible and (2) be as correct as possible.

### [hypothesis](https://hypothesis.readthedocs.io/en/latest/) (or [property-based testing](https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237) more generally)

This is more of a thematic pointer rather than a library per-say but when writing numerical algorithms, we often want to test specific functions (e.g. likelihoods) against a wide range of input parameters. I still probably don't write tests as much as I probably should but relying on smart software to evaluate bugs when dealing with extreme parameter choices is very useful for locking down and testing core functions to make sure that you have guaranteed behavior. 

The first library I encountered for this was the excellent [hypothesis](https://hypothesis.readthedocs.io/en/latest/) library for Python. The abiity to simply set ranges for inputs and handling of different types is really quite amazing to completely battle-test numerical code. It doesn't work as well for more nuanced object-oriented testing - base `pytest` can still be really great there - but works like a dream for more numerical functions. I would definitely recommend using this library to validate your functions against well-constructed inputs for finding trickier edge-cases.

These sorts of "checks against specs" are a much more common framing in functional programming languages where you have strongly defined types and notions of correctness. It just so happens that much of research code in modern biology is written in more dynamically typed languages (e.g. `python`), but applying these tools can be equally fruitful in this setting and worth adding to your toolkit.   

### [`pre-commit`](https://pre-commit.com/)

This is somewhat of a repeat from before but its too good to ignore and something lots of folks getting into computational biology for their first project may not encounter for a while. In computational biology it is perhaps less common to care a lot about code style or interpretabilty, but using something like [`pre-commit`](https://pre-commit.com/) can allow you to ensure that your code is readable and interpretable [^1]. It also very nicely just automatically reduces variability in styles to a recognized standard across languages which is great! 

Some clear benefits of using these tools are: 

* Can instantly make your code easier to read
* Makes it easier to collaborate on coding projects since you have agreed standards on style
* Can ensure robust documentation and sufficient commenting for reproduceability

In many ways this gets to the "lazy" programmer aspect since `pre-commit` will be quite direct in what you need to fix in your code or documentation, rather than you having to come to that realization in 2-5 days or so. You can also customize your experience quite a lot here. 

Once you set this up (even for one-off-scripts), it takes maybe 1-2 months before you automatically start to adopt the style guidelines and have to rely on it much less. I would definitely recommend this tool for researchers who want to ply their craft in an industry setting as well since you might be working on more shared products and this can be useful for building your coding habits more diligently. 


## Productivity Tools 

Admittedly my previous [tools](https://aabiddanda.github.io/blog/2020/12/08/tools) in this realm have been quite "effective"[^2] and its been still helpful. These combined with effective management of your calendar and living based on your calendar during the workday can be quite nice since at the end of the workday you know you were somewhat structured[^3]


[^1]: There are lots of researchers who care a lot about this - but generally speaking with the frequency at which analyses are required, style and interpretability frequently can take a backseat.
[^2]: Productivity is a strange thing to optimize for in life - more recently its just trying to not burn out and schedule truly relaxing breaks.
[^3]: Things can just arise, but try to only let near-term things derail your day as much as you can!