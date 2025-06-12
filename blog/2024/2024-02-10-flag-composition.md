# Is the Maryland flag a design outlier?

<!-- # tags: [flags, PCA] -->


I've lived in Maryland for ~2 years now and have always been amazed at two things immediately since moving here: 1) crabs and Old Bay really set the tone of "Maryland" in a very philosophical way and 2) there is a lot of pride in the Maryland flag in daily life. Like *a lot* of pride for the Maryland flag - much more than any other state that I've ever lived in. I've seen many more of these flags on houses, bumper stickers, and merchandise than I ever thought I would see for a state flag.  

On the face of it -- the flag seems quite unique in design. With a majority color combination that is not common across a number of US flags (red, black, gold) and a distinct lack of a shade of blue that is on most flags. The checkerboard pattern is also quite unique across flags. 


```{image} ../../images/blog_images/flags/md.png
:width: 400px
:height: 300px
:align: center
```
<center>Old Bay, crabs, and a surreal flag.</center>
<br>

This *fascination with the fascination* of [Marylanders with their state flag](https://wamu.org/story/18/03/13/hot-mess-mesmerizing-marylands-state-flag-looks-distinct/), along with some [recently re-designed state flags](https://www.americanflags.com/blog/post/us-state-flag-redesign-movement), made me wonder about whether the Maryland flag really is as much of an aesthetic outlier as I thought? To systematically look at this, I got a set of images of the US state flags (as of 2023) and started some exporatory data analysis. 

Rather than just using the RGB pixel values as features, I used a [common image feature extractor](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_daisy.html)  to try to better capture certain patterns (like the checkerboard like pattern, or symmetry along the diagnonal). I first started with PCA of these features across all US flags: 


```{image} ../../images/blog_images/flags/pca_daisy.us_flags.png
:width: 400px
:height: 300px
:align: center
```
<center>Maryland doesn't immediately seem like an outlier...</center>

<br>

```{image} ../../images/blog_images/flags/md_loading.pca.png
:width: 400px
:height: 300px
:align: center
```
<center>The loadings on the PCs only are extreme on PC17</center>


But when we look at just PC17, the Maryland flag is certainly on the extreme but that PC only explains two percent of the variance! It is possible that more reliable image feature extraction that specifically focuses on shapes may have a stronger ability to separate these flags. 

```{image} ../../images/blog_images/flags/pca_daisy.pc17.png
:width: 450px
:height: 400px
:align: center
```
<center>Maryland is an extreme on PC17.</center>

<br>

```{image} ../../images/blog_images/flags/example.pc17.png
:width: 500px
:height: 100px
:align: center
```
<center>Examples of flags on the extremes of PC17</center>


So its not immediately clear from a data perspective that Maryland has a flag that is stylistically an extreme! It'll always be a wild (yet unforgettable) flag in my mind though. If you're interested in recreating these analyses you can [download the US Flags PNGs](https://flagpedia.net/us-states/download) and follow this [notebook](https://gist.github.com/aabiddanda/875e87f5dd9700e1033886156573e3c2) with my code.
