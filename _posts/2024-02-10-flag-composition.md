---
layout: post
title: "Flag composition analyses"
description: "Fun with flags"
tags: [flags, PCA]
---

<style>
.figure {
  display: table;
  margin: auto;
}

.figure img {
  max-width: 100%;
}

.figcaption {
  display: table-caption;
  caption-side: bottom;
  background: white;
  padding: 10px;
}
</style>


I've lived in Maryland for ~2 years now and have always been amazed at two things immediately since moving here: 1) crabs and old bay really set the tone of "Maryland" and 2) a lot more pride in the Maryland flag in daily life. Like *a lot* of pride for the Maryland flag - much more than any other state that I've ever lived in. 

On the face of it -- the flag seems quite unique in design. With a majority color combination that is not common across a number of US flags (red, black, gold) and a distinct lack of a shade of blue that is on most flags. The checkerboard pattern is also quite unique across flags. 

<figure class="figure">
  <img src="/images/blog_images/flags/md.png" width="400" height="300" alt="">
  <figcaption class="figcaption">Old Bay, crabs, and a surreal flag.</figcaption>
</figure><br>


This *fascination with the fascination* of [Marylanders with their state flag](https://wamu.org/story/18/03/13/hot-mess-mesmerizing-marylands-state-flag-looks-distinct/), along with some [recently re-designed state flags](https://www.americanflags.com/blog/post/us-state-flag-redesign-movement), made me wonder about whether the Maryland flag really is as much of an aesthetic outlier as I thought? To systematically look at this, I got a set of images of the US state flags (as of 2023) and started some exporatory data analysis. 

Rather than just using the RGB pixel values as features, I used a [common image feature extractor](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_daisy.html)  to try to better capture certain patterns (like the checkerboard like pattern, or symmetry along the diagnonal). I first started with PCA of these features across all US flags: 

<figure class="figure">
  <img src="/images/blog_images/flags/pca_daisy.us_flags.png" width="450" height="400" alt="">
  <figcaption class="figcaption">Maryland doesn't immediately seem like an outlier...</figcaption>
</figure><br>


<figure class="figure">
  <img src="/images/blog_images/flags/md_loading.pca.png" width="450" height="150" alt="">
  <figcaption class="figcaption">The loadings on the PCs only are extreme on PC17</figcaption>
</figure><br>


But when we look at just PC17, the Maryland flag is certainly on the extreme but that PC only explains two percent of the variance! It is possible that more reliable image feature extraction that specifically focuses on shapes may have a stronger ability to separate these flags. 

<figure class="figure">
  <img src="/images/blog_images/flags/pca_daisy.pc17.png" width="450" height="400" alt="">
  <figcaption class="figcaption">Maryland is an extreme on PC17.</figcaption>
</figure><br>

<figure class="figure">
  <img src="/images/blog_images/flags/example.pc17.png" width="500" height="100" alt="">
  <figcaption class="figcaption">Examples of flags on the extremes of PC17</figcaption>
</figure><br>

So its not immediately clear from a data perspective that Maryland has a flag that is stylistically an extreme! It'll always be a wild (yet unforgettable) flag in my mind though. If you're interested in recreating these analyses you can [download the US Flags PNGs](https://flagpedia.net/us-states/download) and follow this [notebook](https://gist.github.com/aabiddanda/875e87f5dd9700e1033886156573e3c2) with my code.
