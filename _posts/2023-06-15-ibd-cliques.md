---
layout: post
title: "Identity-by-Descent Cliques"
---

# An Introduction to Identity-by-Descent (IBD)

## Pairwise IBD

With dense genotyping data or whole-genome sequencing data we can begin to better probe the relatedness of a given set of $N$ individuals.Measures of genetic relatedness have a large history in human and population genetics, and all serve to infer or approximate the pedigree of the individuals in your sample.

One popular (and intuitive) measure of relatedness has been to look at the number and size of "blocks" of DNA that are shared between individuals and are inherited from a common ancestor, as shown in the figure below. First we can intuitively describe what we might expect the length of a block to signal. Siblings on average share half of their genome, resulting in very long IBD blocks between siblings. The number of blocks that are shared between two individuals also indicates how related they are (although if the individuals are very closely related, there will likely be a few very large blocks).

<!-- TODO : have a figure describing IBD here -->

Therefore, with advances in being able to detect such blocks from genotype data we have been able to develop a lot of theory for how these pairwise blocks should be distributed amongst samples. Without going through the pain of condensing at least 5 (likely more) papers on the distribution of IBD blocks in unrelated samples of individuals, I will only detail the distributions that are absolutely essential, opting for intuitive results when necessary.

## IBD Cliques

In comparison to pairwise patterns of IBD which are only between pairs of individuals, IBD cliques can be defined as the higher-order analogs of shared IBD segments.

<!-- TODO : show the concept of an IBD clique  here as opposed to pairwise patterns -->

While the theory is clear for pairwise patterns of IBD, the expectations and results for higher-order IBD cliques is less well developed. Also from an information-theoretic standpoint it is interesting to consider whether incorporating these higher order components add any information to improve any sort of meaningful population genetic inference.

For instance, we can ask: given an underlying marginal gene tree, how many 3-cliques of IBD segments would I see that are larger than a certain length threshold?[^1]. However, its also fair that a marginal IBD-clique, where "marginal" just means centered on a location in the genome, will potentially be defined on a much shorter length scale than pairwise IBD segments. This is due to the fact that you may have "offsets" in the IBD blocks that are shared across individuals (even though they may share a common "core" haplotype from a common ancestor), like in Figure 1 below. 

However, we can develop an approximation for the expected length of a shared "core" haplotype amongst $$k$$ lineages. Conditional on the total branch length of the subtree $$\mathcal{L}_k$$, we can then roughly approximate the distance to the left until the core haplotype is broken as an exponential $$l | L_k \sim Exp(-rL_k)$$. Treating the total length of the core haplotype as a sum of two exponentials we arrive at the conditional 

$$b | \mathcal{L}_k \sim \text{Erlang}_2(-r*\mathcal{L}_k)$$ 



<!-- Include a figure of a 3-clique of IBD -->

## Summaries of Pairwise and IBD-Clique Distributions

We consider below a couple of 



## Equilibrium IBD under different models of Population Structure

We hypothesize that IBD cliques will be particularly relevant 



# Sources

- [Palamara et al 2012]() : "TITLE : TBD" *AJHG*
- [Alcala et al 2017]() *bioRxiv*
