---
layout: page
permalink: /research/
title: Research
---


{% assign thumbnail="left" %}

{% for pub in site.data.pubs %}
[**{{pub.title}}**]({{pub.url}})<br/>
{{pub.authors}} <br/>
<i>{{pub.journal}}</i> ({{pub.year}})

{% endfor %}
