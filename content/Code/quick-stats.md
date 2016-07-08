Title:  Quick Terminal Statistics
Date:   2015-12-28 20:19:43
Tags: terminal, statistics, awk

Since I do computational research, I spend a great deal of my day at the command-line. It tends to be slightly annoying when I have to go into R or python and read in a file just to get a summary of a single column of data to make sure that something is not wrong with the analyses. I like to err on the cautious side and check the data that I am working with fairly frequently.

I wrote two versions of a function to get summary statistics on a particular column of data (really simple ones), one using R and one using [mawk]("http://invisible-island.net/mawk/"). [Mawk]("http://invisible-island.net/mawk/") is a variant on the ever-popular awk command-line utility that has been optimized for a subset of awk commands and is noticeably faster in most cases.  

## Using R:

[gist:id=c4ecc4ce9b995aee3b5c,file=rsummary.sh]

*Note : Yes, `--slave` is a real flag for R*

## Using mawk :

[gist:id=c4ecc4ce9b995aee3b5c,file=mawkstats.sh]

For a comparison of the methods, I ran both functions on a 231 MB file representing phased genotypes from Chromosome 22 of the [1000 Genomes Consortium](http://www.1000genomes.org/) Phase 3 data. I used the functions `rsummary` and `mawk_stats` to calculate summary statistics of the phenotype across individuals, which I simulated using R.

The comparison of the two functions (along with a version of `mawk_stats` that uses awk) can be shown by the below screenshot. 

![StatComparison](/images/blog_images/quick_stats_comparison2.png)

It is clear that using `awk` gains us a little speed over the version in R, but that could be attributable to the fact that we do not compute the median or quartiles. However, when we move to using `mawk` we see a huge speedup (2 seconds vs. 19 seconds).

An epilogue to this brief adventure is that while the version of `mawk_stats` is quite a bit faster than the R counterpart, it is missing some crucial information. Future directions would be to implement [Hoare's Selection Algorithm](https://en.wikipedia.org/wiki/Quickselect) using mawk to get the median efficiently and then calculate the quartiles as well. Recursion in (m)awk is a little bit tricky and I will likely devote an entire note to this implementation in the (somewhat) near future. 
