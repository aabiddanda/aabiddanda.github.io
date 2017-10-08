---
layout: post
title: "Quick Summary Statistics in the Terminal"
description: "Tricks in Awk"
tags: [statistics, awk]
---

I spend a great deal of my day at the command-line. Therefore, it tends to be slightly annoying when I have to go into R or python and read in a file just to get a summary of a single column of data to make sure that something is not wrong with my analyses. I like to err on the cautious side and check the data that I am working with fairly frequently. So coming up with some sets of shell commands that might be able to compute summary statistics from text-based data-tables would make things go a little more seamlessly.

I wrote two versions of a function to get summary statistics on a particular column of data (really simple ones), one using R and one using [mawk]("http://invisible-island.net/mawk/"). Mawk is a variant on the ever-popular [awk](https://www.gnu.org/software/gawk/manual/gawk.html) command-line utility that has been optimized for a subset of commands and is much faster in most cases.

## Using R:

{% highlight bash %}
#Usage : <file> <column>
rsummary(){
	R --vanilla --slave -e 'library(data.table); t <- fread("'$1'"); summary(t$V'$2')'
}
{% endhighlight %}


## Using mawk :

{% highlight bash %}

#Usage : <file> <column>
mawk_stats(){
	file=$1
	col=$2
	mawk -v c=$col '{if(min==""){min=max=$c};
		if($c > max){max=$c}; if($c < min){min=$c}; sum+=$c; n+=1}
		END {printf "Min\tMax\tMean\tN\n%.3f\t%.3f\t%.3f\t%.0f\n",min, max ,sum/n, n}' $file
}

{% endhighlight %}


For a comparison of the methods, I ran both functions on a 231 MB file of  phased genotypes from Chromosome 22 of the [1000 Genomes Consortium](http://www.1000genomes.org/) Phase 3 data. I used the functions `rsummary` and `mawk_stats` to calculate summary statistics of the phenotype across individuals, which I simulated using R.

The comparison of the two functions (along with a version of `mawk_stats` that uses awk) can be shown by the below screenshot.

![StatComparison](/images/blog_images/quick_stats_comparison2.png)

It is clear that using `awk` gains us a little speed over the version in R, but that could be attributable to the fact that we do not compute the median or quartiles. However, when we move to using `mawk` we see a huge speedup (2 seconds vs. 19 seconds).

An epilogue to this brief adventure is that while the version of `mawk_stats` is quite a bit faster than the R counterpart, it is missing some information. Future directions would be to implement [Hoare's Selection Algorithm](https://en.wikipedia.org/wiki/Quickselect) using mawk to get the median efficiently and then calculate the quartiles as well. Recursion in (m)awk is a little bit tricky and I will likely devote an entire note to this implementation in the (somewhat) near future.
