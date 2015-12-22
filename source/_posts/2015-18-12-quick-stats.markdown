---
layout: post
title:  "Quick Terminal Statistics"
description: "Getting summary statistics on data without leaving the terminal"
date:   2015-12-17 19:19:43
keywords: "terminal, statistics, awk"
category: code snippet
comments: false
---

Since I do mainly computational research, I spend a great deal of my day at the command-line. So it tends to be a little annoying when I have to go into R or python and read in a file just to get a summary of a single column of data to make sure that something is not off within the data. 

I wrote two versions of a function to get such summary statistics (really simple ones), one using R and one using [mawk]("http://invisible-island.net/mawk/"). Mawk is a variant on the ever-popular awk command-line utility that has been optimized for a subset of awk commands and is noticeably faster in most cases.  

Using R:

{% highlight bash tabsize=2 %}

# Usage : rsummary <filename> <columnnumber>
rsummary(){ R --vanilla --slave -e 'library(data.table); t <- fread("'$1'"); summary(t$V'$2')' }

{% endhighlight %}

using mawk :
{% highlight bash tabsize=2 %}

# Usage: mawk_stats <filename> <column number>
mawk_stats (){
	file=$1
	col=$2
	mawk -v c=$col '{if(min==""){min=max=$c}; 
		if($c > max){max=$c}; if($c < min){min=$c}; sum+=$c; n+=1}
		END {printf "Min\tMax\tMean\tN\n%.3f\t%.3f\t%.3f\t%.3f\n",min, max ,sum/n, n}' $file
}

{% endhighlight %}

For a comparison of the methods, I ran both functions on a 231 MB file representing phased genotypes from Chromosome 22 of the [1000 Genomes Consortium](http://www.1000genomes.org/) data. I used the functions to calculate the mean phenotype of each individual, which I simulated a phenotype \\(Y\\) as \\(Y \sim N(0,5)\\).

The comparison of the two functions (along with a version coded in awk) can be shown by the below screenshot on my laptop. 

![Test Screenshot]({{ "/images/blog_images/quick_stats_comparison2.png" | prepend: site.baseurl }})
*The top version is with mawk, the middle with awk, and the last with R*

It is clear that using awk gains us a little speed over the version in R, but that could be attributable to the fact that we do not compute the median or quartiles. However, when we move to using `mawk` we see a huge speedup. 

Future directions would be to implement [Hoare's Selection Algorithm](https://en.wikipedia.org/wiki/Quickselect) in mawk (if possible) to get the median efficiently and then calculating the quartiles. This would get us to display all the information that R is able to but much faster! 



