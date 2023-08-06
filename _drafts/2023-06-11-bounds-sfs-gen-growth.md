---
layout: post
title: "Bounds on Site-Frequency-Spectrum based Inference in Generalized Growth Models"
description: " "
tags: [site frequency spectrum, generalized growth, theoretical population genetics]
---

# The Site Frequency Spectrum

In plain terms, the site-frequency spectrum (SFS) is the histogram where the x-axis represents the number of derived (non-ancestral) alleles that are carried \\( n \text{to} n-1 \\)[^1], and the height of each bar is the density of how many mutations fall into this particular class.

[1]: This is known as the "unfolded" SFS, because we have an idea about whether the allele is derived or ancestral. If we did not have this information we would only have a SFS up to \\(\frac{n}{2}\\) which is known as the  "folded" SFS.

The SFS is a fundamental summary statistic used in population genetics, since the distribution of derived alleles in a given sample is influenced by evolutionary forces such as demography and selection.

<!-- TODO : image of the SFS -->

In the remainder of this blog post I make the following assumptions:

 * The infinite-sites model holds - a single site is only ever allowed to mutate once in the genealogical history of the sample.
 * The SFS reflects neutral evolution, so demography (genetic drift) is the only force affecting the SFS.
 * Each site evolves independently, so there is no correlation between the \\( s \\) sites that we use to construct our SFS (e.g. linkage equilibrium)

From the following assumptions that we have made here, we would like to ask a seemingly simple question : "What are the information-theoretic bounds on using statistics based on the SFS for inferring the demographic history of the population"?

# Inferring Demographic History from the SFS

<!-- TODO : review polanski and kimmel results, for fast computation -->

<!-- TODO : review terhorst and song work here, plus that of EGGS -->

<!-- From the results put above, it seems that sample size matters not, just that the amount of "genomic real estate" that you have that is variable \\( s\\). However in practical terms for the genomes of eukaryotes that undergo meioses, the genome has correlations within it due to inheritance occurring in a block like fashion. -->


# Information Theoretical Bounds




# Bounds under a generalized growth model

<!-- TODO : describe the equation for generalized growth -->

One feature of many human populations around the globe is that there has been rapid 'explosive' growth[^2] in the recent past. A major question is how this affects the genetic diversity that we see in present day individuals, and subsequently how we can use present-day genetic variation to infer these patterns of explosive growth.

[2]: By 'explosive' we mean that the population is growing at a rate faster than exponential. Note that the model we explore here is not the only model of growth that is possible, as there are alternative models in the limits of larger offspring sizes and such (see Eldon and Wakeley for a description of some of these models)

Before we begin asking how 'explosive growth' can affect patterns of genetic diversity, we would like to have parameterized models that reflect this faster than exponential growth. We can use the following differential equation for the population size put forth by Reppell et al :

$$ \frac{dN}{dt} =  - \alpha N_i^\beta $$

When we solve for this, we get a function of the form:

$$
\begin{cases}
  \left(N_i^{1-\beta} - \alpha t (1 - \beta)\right)^{\frac{1}{1 - \beta} } & \beta \neq 1 \\
  N_ie^{-\alpha(t)}& \beta = 1
\end{cases}
$$


We can interpret \\( \beta \\) as a 'growth speed' parameter that when it is greater than 1, the growth is faster than exponential growth.

![gen_growth](/images/blog_images/gen_growth.png)
*An Example Generalized Growth Model*

From the plot above, we can see both details of "super-exponential" growth (\\( \beta > 1\\)) and "sub-exponential" growth (\\( 0 < \beta < 1\\)). We would primarily like to look at the minimax error bounds when using the SFS in order to infer generalized growth patterns.

##  Deriving Minimax bounds for Generalized Growth

<!-- TODO : mention that Terhorst and Song primarily consider piecewise constant models -->

The two main scenarios that Terhorst and Song cover are (1) piecewise-constant demographies and (2) exponential growth.  


Here we would like to consider a scenario where each epoch of the demographic history is defined by a generalized growth function



## Caveats


# Discussion

While there is a decent amount of math in this post, the overall problem is one that a lot of theoretical population geneticists have devoted themselves to over the years, namely: how do we use patterns of genetic variation in a sample to estimate population sizes in the past?

The secondary question that we care about when applying calculations to data are: (1) Are we maximizing the information present in the genetic data to make our inferences? (2) Is it possible to devise statistics that come close to theoretical limits?

We should acknowledge that some of the simplifying assumptions made above are "information-limiting", in the sense that they throw away important aspects of genomic information that would be valuable to model. A prime example of this is the assumption that each site is uncorrelated, which is not the case in eukaryotic genomes due to linkage disequilibrium. With the advent of readily available whole-genome sequencing (WGS) data modeling the correlations between sites in addition to the mutational history has proven to be a productive avenue of inquiry for the field, resulting in methods like PSMC, MSMC, and SMC++ <CITE>.

Given the wide usage of the SMC (and SMC') approximation in modern population genetic analyses, it seems compelling to devise information-theoretic bounds on estimating demographic history within this set of models as well. A practical motivation for this is that methods such as PSMC and MSMC are orders of magnitude more computationally costly than methods to estimate demography via the SFS.

# References

* Myers paper on SFS-based inference methods
* Polanski and Kimmel
* Terhorst et al
* Bhaskar and Song
* Gao and Keinan
* Reppell et al

# Resources

I have created plots of the information theoretic bounds discussed here for both the piecewise-constant and generalized-growth case in a jupyter notebook that can be accessed [here].
