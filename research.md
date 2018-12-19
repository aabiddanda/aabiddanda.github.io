---
layout: page
permalink: /research/
title: Research
---

My research interests span both theoretical and applied population genetics - particularly within humans. Much of this research is motivated by both the increasing availibility of diverse genomic data types (e.g. ancient DNA) and studies of complex traits. Some recent topics of interest have been:
	
* The demographic history of isolated populations
* The spatial / geographic distribution of functional genetic variants
* The spatial distribution of variants shared between ancient and modern samples
* Multi-locus models of genetic variation with serial sampling


# Publications 

{% assign thumbnail="left" %}

{% for pub in site.data.pubs %}

[**{{pub.title}}**]({{pub.url}})<br/>
{{pub.authors}} <br/>
<i>{{pub.journal}}</i> ({{pub.year}})

{% endfor %}
