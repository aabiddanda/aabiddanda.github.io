---
layout: page
permalink: /research/
title: Research
---

<!--TODO : at some point should break this down into sections -->
My research interests span both theoretical and applied population genetics - particularly within humans - and its influence on complex phenotypes. Some recent topics of interest have been in the demographic history of isolated populations, the geographic distribution of functional alleles, and the spatial distribution of variants shared between ancient and modern samples.

# Publications 

{% assign thumbnail="left" %}

{% for pub in site.data.pubs %}

[**{{pub.title}}**]({{pub.url}})<br/>
{{pub.authors}} <br/>
<i>{{pub.journal}}</i> ({{pub.year}})

{% endfor %}
