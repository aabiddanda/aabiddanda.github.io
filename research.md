---
layout: page
permalink: /research/
title: Research
---

My research interests span both theoretical and applied population genetics - particularly within humans. Much of this research is motivated by both the increasing availibility of diverse genomic data types (e.g. ancient DNA) and studies of complex traits. Some recent topics of interest have been:
	
* The demographic history of isolated populations
* The spatial distribution of variants shared between ancient and modern samples
* Multi-locus models of genetic variation with serial sampling
* Statistical genetic methods for biobank-scale data

# Publications 

{% assign thumbnail="left" %}

{% for pub in site.data.pubs %}

{% if pub.pdf and pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [[PDF]({{pub.pdf}})] [[Software]({{pub.software}})]
{% elsif pub.pdf %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [[PDF]({{pub.pdf}})] 
{% else %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
{% endif %}

{% endfor %}
