---
layout: page
permalink: /publications/
title: Publications
---

{% assign thumbnail="left" %}

<sup>* indicates equal contribution</sup>

<!-- ### Navigation
[Preprints](#Preprints) [2023](#2023) [2022](#2022) [2020](#2020) [2018](#2018) [Older](#2016) -->

<!-- ## Preprints 
{% for pub in site.data.pubs %}

{% if pub.journal == "bioRxiv" %}

{% if pub.pdf and pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}})<br/>
  [Software]({{pub.software}})
{% elsif pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [Software]({{pub.software}})
{% elsif pub.pdf %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}})
{% else %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
{% endif %}

{% endif %}

{% endfor %} -->


<!-- Define the years here -->
{% assign years = "2024, 2023, 2022, 2020, 2018, 2016, 2015" | split: ", " %}

{% for year in years %}
## {{year}}

{%  for pub in site.data.pubs %}

{% if pub.journal != "bioRxiv" and pub.journal != "Report" and pub.year == year %}

{% if pub.pdf and pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}})<br/>
  [Software]({{pub.software}})
{% elsif pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [Software]({{pub.software}})
{% elsif pub.pdf %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}}) 
{% else %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
{% endif %}

{% endif %}

{% endfor %}

{% endfor %}


## Technical Reports 

{% for pub in site.data.pubs %}

{% if pub.journal == "Report" %}

{% if pub.pdf and pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}})<br/>
  [Software]({{pub.software}})
{% elsif pub.software %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [Software]({{pub.software}})
{% elsif pub.pdf %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
  [PDF]({{pub.pdf}}) 
{% else %}
  [**{{pub.title}}**]({{pub.url}})<br/>
  {{pub.authors}} <br/>
  <i>{{pub.journal}}</i> ({{pub.year}})<br/>
{% endif %}

{% endif %}

{% endfor %}


