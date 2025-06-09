
# A Reading List for Statistical / Population Genetics

Over the course of graduate school I noticed that I started to gravitate repeatedly towards particular references as starting points for questions. This is a list of some favorite readings of mine that have been particularly thought-provoking for my research or useful for understanding human genetics in a broader societal context. 

## Human History and Genomics

* [Tracing the peopling of the world through genomics (Nielsen et al 2018)](https://www.ncbi.nlm.nih.gov/pubmed/28102248)

  An article describing at a high level the major events over the span of human history as we have learned from genomic data in modern and ancient human samples. Figure 3 in particular is a great one to think at a more broad level about the timing and extent of major human expansion waves. 

* [A Population-Genetic Perspective on the Similarities and Differences among Worldwide Human Populations (Rosenberg 2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3531797/)
  
  This is a paper that I refered to a lot when asking questions about how frequent human genetic variants might be in different parts of the world and how they relate to demographic history. The results here are superseded in some sense by the data presented in the [updated HGDP paper](https://science.sciencemag.org/content/367/6484/eaay5012) but the themes largely still hold.

## Population Genetic Models

* [Gene genealogies and the coalescent process (Hudson 1991)](http://home.uchicago.edu/rhudson1/popgen356/OxfordSurveysEvolBiol7_1-44.pdf)
  
  One of the fundamental models I use for modeling genetic variation is the coalescent process. This chapter by Richard Hudson is a really great resource for starting out. For a meatier resource, I have used John Wakeley's excellent [book](https://www.amazon.com/Coalescent-Theory-Introduction-John-Wakeley/dp/0974707759 ) on the subject as a consistent resource as well. 


* [A Markov Chain Model of Coalescence with Recombination (Simonsen & Churchill 1997)](https://www.ncbi.nlm.nih.gov/pubmed/9356323)
  
  A large portion of my time in graduate school was spent thinking about coalescence models with recombination. The model proposed here is a great starting point as it describes the backward in time process as a Markov Chain model that requires little in the way of preliminaries. The work proposed here is extended upon in [further work](https://www.ncbi.nlm.nih.gov/pubmed/24486389) describing the process after conditioning on the tree at one locus and ["Phase-Type" distributions](https://www.sciencedirect.com/science/article/pii/S0040580919300140) for these joint tree properties. 

* [Inference of Population Splits and Mixtures from Genome-Wide Allele Frequency Data  (Pickrell & Pritchard 2012)](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1002967) 

  This was one of the first population genetic modeling papers where I used the resulting software on an empirical dataset. However, this paper frames how allele frequency differences accumulate across branches of a population phylogeny based on a [previous model]. This model using a multivariate-normal approximation is very useful trick to nicely calculate how much we may expect allele frequencies to differentiate between populations. 

* [Modeling linkage disequilibrium and identifying recombination hotspots using single-nucleotide polymorphism data (Li & Stephens 2001)](https://www.ncbi.nlm.nih.gov/pubmed/14704198)
  This paper was another cornerstone of my learning in graduate school, and has been the basis for a number of central methods in statistical population genetics (e.g. imputation, phasing). In my opinion this paper and the supplement of the `fineStructure` [paper](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1002453) really nicely capture the structure of these haplotype-copying models and their framing as a hidden markov model. 
  
## Statistical Genetics

* [False discovery rates: a new deal (Stephens 2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5379932/)

  This paper was a great way that I learned a lot of statistical concepts like mixture models, false sign rates, and FDR. The modeling framework is also really nice for trying to frame GWAS summary statistics because you often get just effect-sizes and their standard errors. 

* [High-Resolution Mapping of Expression-QTLs Yields Insight into Human Gene Regulation (Veyrieras et al) ](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000214) 

  This paper propposes a clever hierarchical model to incorporate additional annotations (or genomic features) into mapping of genetic variants responsible for complex traits. With the current efforts to understand the relationship between mapping and functional genetic data this is a useful framing on how annotations can impact trait association signals
  

## History of Science & Popular Science

* [The Origins of Theoretical Population Genetics (William B. Provine)](https://www.amazon.com/Origins-Theoretical-Population-Genetics/dp/0226684644)

   Much of the early debates in population genetics were centered on the extent and mode of evolutionary change (drift vs. selection, additivity vs. epistasis, discrete shifts vs. quantitative and graduate change). Provine's work here provides a lot of context for the history of population genetics as well as a great way to revisit how the field was before the explosion in molecular data.   

* [Human Diversity (Richard Lewontin)](https://www.amazon.com/Human-Diversity-Scientific-American-Library/dp/0716760134)

  This is a great popular science book by Lewontin highlighting broad patterns of human genetic diversity. Its also a good read to educate others on the relative differences between different human groups and how it relates to differences at the genetic level. 

* [Imbeciles : The Supreme Court, American Eugenics, and the Sterilization of Carrie Buck (Adam Cohen)](https://www.amazon.com/Imbeciles-Supreme-American-Eugenics-Sterilization/dp/0143109995)

  One of the more sordid parts of human genetics research is its role in the justification of eugenic practices. This book by Adam Cohen provides a glimpse into the legal aspects surrounding eugenics in 1920s America. Its a good read to highlight how research can be misappropriated with consequences that affect human lives, and to engage your own research to avoid such problems.  

