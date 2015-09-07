---
layout: post
title:  "Stats with Awk"
date:   2015-07-15 22:37:23
categories: snippet
---

<div align="left">

{% highlight bash tabsize=2 %}
	# Usage : stats_awk <filename> <columnnumber>
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
Reading a large data table into R can take an agonizingly long time, especailly if you just want some quick summary statistics of one column of data. Let this function do things faster for you. Consider using <strong><a href="http://invisible-island.net/mawk/">mawk</a></strong> for higher performance. 
</p>

<p>
<strong>EDIT:</strong> 

Using the <strong> <a href="https://cran.r-project.org/web/packages/data.table/index.html">data.table</a></strong> package in R yields times that are close (but still not as fast) to the implementation above with <strong><a href="http://invisible-island.net/mawk/">mawk</a></strong> but you get more summary statistics. The function is below:

{% highlight bash tabsize=2 %}

# Usage : rsummary <filename> <columnnumber>
rsummary(){ R --vanilla --slave -e 'library(data.table); t <- fread("'$1'"); summary(t$V'$2')' }

{% endhighlight %}

</p>	
</div>

