---
layout: page
title: Publications
---

<h4><a target="_blank" href="https://scholar.google.com/citations?user=BWVZXhgAAAAJ&hl=en"> My Google Scholar Page</a></h4>

<ul>
{% for pub in site.data.pubs %}
  <li>
		<p> {{ pub.authors }} <br/>
		<a href="{{ pub.url }}" title="{{ pub.title }}"> {{ pub.title }} <i> ({{ pub.journal }}) </i> </a> <br/>
		({{ pub.date }}) </p> 
	</li>
{% endfor %}
</ul>
