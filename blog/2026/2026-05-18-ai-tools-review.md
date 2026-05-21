# An internal experiment as an AI-skeptic

Since around mid-2024 I had become curious about the role of AI and [LLMs](https://www.ibm.com/think/topics/large-language-models) specifically in how it might improve how I do science. Given that it was being used quite judiciously across multiple biological disciplines --- including pharmaceutical research and development --- it seemed like a nice time to test out an agent and see how it has changed my working habits a bit over a two month period. I have been using Claude Pro for all of these tests and haven't really been interested in testing out the broader swath of tools out there. The structure of my internal experiment was to basically ``use AI however I deemed fit '', and at the end kind of justify whether it was worth the price to me (personally paying $20 a month, or like 4 cafe espresso drinks in Washington, DC).

This blogpost is not really meant to be an endorsement of using AI broadly in academic science, more of my own experiences with it and where I have found it specifically helpful. For a broader overview, this [substack post from Ran Blekhman](https://blekhman.substack.com/p/you-need-to-make-ai-guidelines-for) was very useful to read prior to starting my two month experiment. 

I won't go through the pros/cons of using AI as directly in this blogpost. I have structured the post more to focus on the *roles* of AI that I found most (and least) helpful in my experience over my scientific life over the past two months and whether I think it was worth it overall.


#### Role 1: The Writing Reviewer / Editor 

I would say that academic writing is *annoying* to read at best, and sometimes *infuriating* to produce. However, there is a ton of value in having a soundboard for your writing in the form of AI. It can adapt to different styles (e.g., Grants, Review article, Research Article) and provide you feedback on individual paragraphs. My rough rule here is that 1) it is better to write some junk as your first draft that is genuinely your words, even if it is painful to read and 2) AI is a really helpful reviewer/editor, but do not let it take the first pass wholesale. The second point is somewhat critical, because you want to make sure that ideally what you're writing is not some strange synthesis of other folk's writing and consistent with your tone. 

The most valuable prompts in my experience with this kind of task have been: 

1. *Can you summarize the main point of each paragraph in a sentence, and identify the top 5 locations where there may be thematic redundancies? Specifically if there are clear redundancies across different paragraphs. If you can summarize each paragraph for a broad scientific audience that would be best.*

This one is exceptionally helpful especially for making sure you can tune the verbiage to a specific audience and make sure that at least the AI can *interpret* what you are saying. The asking about redundancies is also really useful to identify places where you can be a bit more brief later on in the manuscript or places where the redundancy can be fully removed. 

2. *Can you provide some alternative sentence structure here which may make the meaning clearer? I specfically mean \[...\]*

This is somewhat of a trick prompt, because you provide a kind of brief statement of what you mean anyways, and the AI can ideally find some kind of middle ground between what you suggested and what you had previously written. Very useful for simplifying your language and sentence structure.

3. *Could you suggest ways to preserve the meaning of each sentence, but to shorten the word count by \[10%\]?*

This one is one that I have used quite a bit especially if you are running afoul of word/character limits. I think that you can obviously tune the percentages in your prompting, but overall at a high level I have found that if you go higher than 20% it is very difficult to preserve the actual meaning of the text. Perhaps that is somewhat obvious! The sweetspot should be around 5-10% for most academic writing.  

#### Role 2: The Figure Design Consultant

I would like to say that I am pretty decent at figure design in my science. I like having TSVs that are easy and straightforward to organize into some key plots and figuring out how to most effectively convey data-centered information. This is not with reference to improving your plotting of *actual data* (not really at least). 

The more (most?) complicated plots in science are what I like to call ``synthesis plots'', where you actually have little to no data, but it should convey a broader ``theme'' of the research or project or finding. If you have ever written for a journal that has required a kind of ``summary'' figure, it is those figures. You sadly cannot `matplotlib`-wizardry your way out of this one!

In instances like this, I have found it very helpful to gather some figures as PNGs from various papers that kind of inspire the work and ask the AI to create a "thematic figure" which reflects this. If you have a passage of text / results that can also be used to synthesize the key figures. Also find some summary figures from papers that you like, and ask it to replicate the figure 

A couple of tips I learned along the way of doing this that I think are somewhat intuitive, but useful nonetheless:

1. **Always ask for some form of vector graphics if you can**. PNGs are great for intermediately putting into google docs, but you want to have at least some control using software like Affinity Designer to secure colorschemes and typefacing. 

2. Ask for suggestions on "paneling" and ratios of panels specifically, because this setup of the initial "layout" can be massively beneficial. It can also be broadly useful to think of how specific panels may lead to information in others. 

3. Try to find certain ``plot elements'' from public online repositories if you can to supplement the AI generated ones during your revisions in an image editor. I have really liked the SVG library from the [NIH BioArt](https://bioart.niaid.nih.gov/) resource as well. These are really useful when you want to avoid any complex licensing issues. 

4. **Bonus** Stylesheets. I have been wanting to make specifically loaded `matplotlib` stylesheets for my figures for a long time. The primary goal was to formally separate out my styling for figures in a paper and the same figure for a presentation. Mainly because figures for papers tend to be a lot more information dense than [those required for a talk](https://rajlaboratory.blogspot.com/2014/04/figures-for-talks-and-figures-for-papers.html). However, making a stylesheet is really quite annoying since you have to specify layouts and fontsizes. What I used AI for specifically was to design a `matplotlib` stylesheet after feeding in a couple PDF versions of slides from talks (16:9 format, [Atkinson HyperLegible Font](https://www.brailleinstitute.org/freefont/)). This allows for very clearly different aesthetics for the same data to improve presentations and visual acuity. 

```{image} ../../images/blog_images/ai/scatter_stylesheets.png
:width: 530px
:height: 230px
:align: center
```
<center>Left side uses the stylesheet for figures, right for presentations.</center>


#### Role 3: The Approximation Specialist

I am *just* good enough at math / statistics to be dangerous (e.g., knowing how to model stuff pretty well). However, with the scales of modern biological datasets, it is often not the modeling aspects but rather identifying approximations which make methods actually tractable and useful. This happens to be just up against my knowledge boundary and I think is a kind of great sweetspot for AI to help you out, since the fun part of mathematical modelling you can do yourself like writing down distributions, but agents can help you with things like computing gradients and approximations. 

As a quantitative researcher, I feel like it is quite important to at least sketch out the likelihood yourself if you can. This way, you at least know how you would *generate* data to represent your observed data. This is a great starting point for now thinking about approximations if you need them. A couple of unsolicited tips for this task: 

1. Always ask for test data when the AI is evaluating the approximation. It is even better if you can provide a direct implementation for the likelihood calculation to benchmark against. Often a saddlepoint approximation or Taylor series type approximation will be extremely useful. 

2. Ask the AI to document and write tests - try to get it to use a ``property-based'' testing framework like [hypothesis](https://hypothesis.readthedocs.io/en/latest/). This definitely helps you identify the extremes where the approximation might actually break down. 

3. Always ask for an expected speedup and check against a test implementation. 

#### Outlook

I think that I was motivated to start this by 1) [FOMO](https://en.wikipedia.org/wiki/Fear_of_missing_out) and 2) a general curiousity whether bringing AI in would make me a more productive/better/consistent scientist. In the early days I was broadly skeptical because of hallucinations and sacrificing the *correctness* of my work (and actually taking away some of the things that I enjoy on the day-to-day). I also want to reiterate that this whole post is just my opinion from a two month stint (which I anticipate lengthening for a little bit at least).

In general, I remain somewhat skeptical of turning to AI wholesale for doing my actual *thinking* --- because I would like to validate any qualitative or quantitative claim that I make in my research. So for that reason I don't think I will be turning to AI for actually writing a first draft or even broader literature reviews in the recent future. Even quantitatively, I have found it is quite good at explaining why specific approximations (e.g., saddlepoints) work well and it is quite satisfying to actually use it as a learning tool a bit. 

What I've highlighted above are clear ways in which AI can be a useful sounding board for improving writing, figures, and in some cases scalability of your research. This is also a great boon for productivity and kind of treating it as a tool for first round of feedback before sending to colleagues to provide further comments which can be kind of nice. It also helped me at least very acutely identify skills I was bad at starting (e.g., making thematic figures), but was ok with doing after the initial version was put together (e.g., editing thematic figures). Finding these reductions in high early activation energy and making sure they pop up frequently enough in your life is critical for yourself to feel like the investment is worth it as an early career researcher. 

I've also found that limiting my AI use to specific windows of time in my calendar blocks is also a little bit more helpful and now trying to block times where I want to be kind of AI-free. I have not relaly kind of found the ideal ratio of this new style of calendar blocking but broadly I think that it works quite well. I am slowly trying out agentic coding to see if it works well for actually building out software implementations of methods (particularly CLIs), and will put in some updates on this in the future. 