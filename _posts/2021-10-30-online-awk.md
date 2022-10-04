---
layout: post
title: "Three helpful algorithms in `awk`"
---

In modern data analysis, the data streams are often so big (on the order of millions of entries) that we often want to have some way to inquire about properties of data elements without having to load the entire dataset into memory. In genomic data analysis, this might be outputting two columns and estimating their correlation, estimating the median of a column, or the number of outliers outside some multiple of the interquartile range.

In terms of swiss-army-knife skills, learning `awk` is an amazing bonus for doing fairly complex things without necessarily having to truly write scripts using `python` or `R` and loading in formal data tables. Eventually you likely will have to do that (you can't make plots with `awk` alone as far as I know), but for quick summary statistics we can use `awk` to get a great sense of your data. In this post I'll cover three snippets that are useful aliases to have on most systems with `awk` so you can reliably manipulate datastreams to your will and more quickly check if your data generation is suspect. 

The key is that we want most of these algorithms to run in time $$\mathcal{O}(n)$$, where $$n$$ is the number of data points that are provided. However, in the spirit of simplicity for some of the downstream algorithms, we have $$\mathcal{O}(n\log n)$$ complexity purely because the code is easier to understand and to take advantage of core Unix utilities.

## Linear-time Algorithm for Correlation 

One of the first things you might want to check may be the correlation between two columns in your data if they're numeric values from a direct stream rather than loading the data into memory. This streaming algorithm is one such way:

{% highlight bash %}
# A port of Welford's online algorithm for correlations ..
function corr(){
	awk '{
		n += 1; 
		x += $1; 
		y += $2; 
		f = 1/n; 
		dx = $1-mx; 
		dy = $2-my; 
		mx += f*dx; 
		my += f*dy; 
		vx = (1. - f)*(vx - f*dx*dx); 
		vy = (1-f)*(vy-f*dy*dy); 
		cxy = (1-f)*(cxy - f*dx*dy);} 
		END {print cxy/sqrt(vx * vy)}' $1
}
{% endhighlight %}


##  Median Algorithm

This is a fairly simple algorithm that will come very close to the median (it won't do the averaging though)

{% highlight bash %}
function median(){
  sort -n | awk 'BEGIN {cnt=0;} { 
     vals[cnt] = $1; cnt++;
     } END {print vals[int(cnt/2)]}'
}
{% endhighlight %}

It's not the fastest solution possible but for some context takes about ~30 seconds for 10 million entries on a 2020 Macbook Air without having to necessarily read a file completely into memory.   

## Outlier Detection via Inter-Quartile Range

One of the typical checks that you might want to do for a data stream would be to check the number of points that fall outside some interquartile range. In order to calculate these interquartile ranges we can then calculate them as below:

{% highlight bash %}
function iqr(){
  sort -n | awk '{
    vals[cnt] = $1; cnt++;
    } END {
      q1=int(cnt/4); 
      q3=int(q1*3); 
      print vals[q1], vals[q3], vals[q3] - vals[q1]
  }'
}
{% endhighlight %}
