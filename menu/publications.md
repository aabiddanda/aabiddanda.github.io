---
layout: page
title: Publications
---

<h4><a target="_blank" href="https://scholar.google.com/citations?user=BWVZXhgAAAAJ&hl=en"> My Google Scholar Page</a></h4>

<!--TODO : need to alter up some of the  styling here  -->
<ul>
{% for pub in site.data.pubs %}
  <li>
    <a href="{{ pub.url }}" title="{{ pub.title }}">
      <h5>
        {{ pub.title }} <i>({{ pub.journal }})</i>
        <span class="icon icon-ios-arrow-thin-right"></span>
      </h5>
    </a>
		<h5>{{ pub.authors }} ({{ pub.date }})</h5>
	</li>
{% endfor %}
</ul>
