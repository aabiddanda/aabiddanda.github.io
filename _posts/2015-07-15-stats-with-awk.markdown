---
layout: post
title:  "Stats with Awk"
date:   2015-07-15 22:37:23
categories: snippet
---


<img class="bg" src="/img/chicago_skyline.jpg">

<div align="left">

{% highlight bash %}

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

<p>
Reading a large data table into R can take an agonizingly long time. Let this function do things faster for you. Consider using <strong><a href="http://invisible-island.net/mawk/">mawk</a></strong> for higher performance. 
</p>
</div>

