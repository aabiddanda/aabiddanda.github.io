---
layout: post
title:  "Stats in Awk"
date:   2015-07-15 22:37:23
categories: snippet
---

<div align="left">

{% highlight bash %}

	# Usage : stats_awk <filename> <column number> 
	stats_awk (){
	file=$1
	col=$2
	mean=$( awk -v c=$col '{sum+=$c} END {print sum / NR "\t" NR}' $file )
	n=$( echo $mean | awk '{print $2}' )
	mean=$( echo $mean | awk '{print $1}' )
	var=$( awk -v c=$col -v a=$avg '{sum+=($c-a)**2} END {print sum / (NR-1)}' $file )
	echo -e "MEAN\tVAR\tN"
	echo -e "$mean\t$var\t$n" 
	}
{% endhighlight %}

</p>
Reading a large data table into R can take an agonizingly long time. Often times we are also just interested in the data in one particular column. The function above computes the mean and variance of a particular column using awk. I plan to post later on some more complicated stats that can be computed using awk. A more high-performance version of awk is mawk, but it only captures a subset of the functionality that awk has. For datatables that are very large (~30-100 MB), the difference between awk and mawk is made apparent. An excellent related post on awk and its particular uses in a bioinfomatics environment can be found here
</p>
</div>
