Title:  Random Graph Theory in Population Genetics
Date:   2016-12-28 19:19:43
Tags: graph theory, IBD
Status: draft

In the fall of my junior year at Cornell, I had the pleasure of taking a class with Jon Kleinberg on the "Structure of Information Networks". Being an overly confident college student, I failed spectacularly, but not in the conventional sense. I got the nice little ``A'' on my transcript, but I understood very little about the content of the course.

Fast forward a couple of years (and a couple of slices of humble pie), and I encountered graph theory being used in the population genetics and computational genetics literature and decided to take the leap into the proverbial rabbit hole once again.

<!-- *TODO : Describe the original IBD network paper by Gusev and colleagues * -->
<!-- *TODO : Describe the proposition by Watts and Strogatz    *    -->

## Identity by Descent (IBD) Networks

Graphs can be used to describe the relationships between individuals within a population, and plays a non-trivial role in modern population genetics. Indeed, the simple pedigrees from introductory genetics and their approximations (e.g. [Kingman's Coalescent](https://en.wikipedia.org/wiki/Coalescent_theory)) are graphs which describe the relationships between your samples.  

<p align="center">
  <img src="/images/blog_images/ibd.png", alt="Test1">
</p>

In the age of personal genomics, a lot of insights about ancestry are driven by the detection of haplotype sharing. The fiIndeed this is the approach taken by 23andMe and AncestryDNA, arguably the two biggest personal genetics companies. The output of these algorithms should be sets of edges (shared IBD segments) between individuals. Since the nodes are defined by the individuals, and the edges are then defined by the sharing of IBD segments. 


<p align="center">
  <img src="/images/blog_images/gusev_mbe2012_fig2.jpg", alt="Test2">
</p>


Now that we have a full-fledged graph, we can start asking questions about features of the graph. Here, I am particularly interested in the degree distribution of the graph. The degree distribution should tell me intuitively how "tightly packed" the graph is. 

 
## Theoretical Results for Degree Distributions on Random Graphs

Under idealized conditions where each edge is placed independently 

$$
\begin{equation}
p_k = \binom{N}{k}p^k(1-p)^{N-k} \approx \lim_{N \rightarrow \infty} \frac{\lambda^k e^{-\lambda}}{k!}
\end{equation}
$$

However it has been shown that for many real-world networks the degree distribution is wildly different from that of a Poisson distribution. 



## A Toy Simulation

Here what we are interested in is if we can use the distribution on the degree within the graph to predict the effects of a bottleneck (and )








## References and Reproducibility

If you would like to recreate the analysis from this post, please see this [Github Repository](https://github.com/aabiddanda/IBD-Networkz). 














