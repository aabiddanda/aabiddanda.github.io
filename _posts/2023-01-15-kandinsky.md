---
layout: post
title: "Visualizing my research using Kandinsky diagrams "
---

<style>
  * {
    box-sizing: border-box;
  }

  /* Position the image container (needed to position the left and right arrows) */
  .container {
    position: relative;
  }

  /* Hide the images by default */
  .mySlides {
    display: none;
  }

  /* Add a pointer when hovering over the thumbnail images */
  .cursor {
    cursor: pointer;
  }

  /* Next & previous buttons */
  .prev,
  .next {
    cursor: pointer;
    position: absolute;
    top: 40%;
    width: auto;
    padding: 16px;
    margin-top: -50px;
    color: white;
    font-weight: bold;
    font-size: 20px;
    border-radius: 0 3px 3px 0;
    user-select: none;
    -webkit-user-select: none;
  }

  /* Position the "next button" to the right */
  .next {
    right: 0;
    border-radius: 3px 0 0 3px;
  }

  /* On hover, add a black background color with a little bit see-through */
  .prev:hover,
  .next:hover {
    background-color: rgba(0, 0, 0, 0.8);
  }

  /* Number text (1/3 etc) */
  .numbertext {
    color: #f2f2f2;
    font-size: 12px;
    padding: 8px 12px;
    position: absolute;
    top: 0;
  }

  /* Container for image text */
  .caption-container {
    text-align: center;
    background-color: #222;
    padding: 2px 16px;
    color: white;
  }

  .row:after {
    content: "";
    display: table;
    clear: both;
  }

  /* Six columns side by side */
  .column {
    float: left;
    width: 16.66%;
  }

  /* Add a transparency effect for thumnbail images */
  .demo {
    opacity: 0.6;
  }

  .active,
  .demo:hover {
    opacity: 1;
  }

</style>

<script>
  let slideIndex = 1;
  showSlides(slideIndex);

  // Next/previous controls
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  // Thumbnail image controls
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("demo");
    let captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
  }
</script>

I've always enjoyed art galleries and museums for their tranquility, and they're really great places to get some valuable "thinking time". I also know that I don't really have a strong eye for art (although [interpretations can clearly be subjective](https://www.youtube.com/watch?v=SZeyrb8SdSA&t=91s)). I've often gotten a lot out of visual abstracts for papers, and I've been curious about AI generated art (e.g. [DALLE](https://openai.com/dall-e-2/)), so naturally I was wondering whether this could be a relatively simple task to generate an "art gallery" of research I've done. 


In this spirit I found the works of [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky) really fascinating, because they have really straightforward and simple ingredients (e.g. sine waves, rectangles, circles) that are oriented in different ways. It also happened to have a very nice [R package](http://giorasimchoni.com/2017/07/30/2017-07-30-data-paintings-the-kandinsky-package/). Its certainly less sophisticated that currently derived machine-learning methods (like variational autoencoders or DALLE), and the downside is that it only generates art in the style of Kandinsky, rather than mimicing the stylings of another artist. The upside is that with a [couple of scripts](https://gist.github.com/aabiddanda/145e52d975549cd2462bc0f930f56d45), you too can generate your own gallery based on your abstract! 

<!-- Container for the image gallery -->
<div class="container">

  <!-- Full-width images with number text -->
  <div class="mySlides">
    <div class="numbertext">1 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.0.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">2 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.1.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">3 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.2.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">4 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.3.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">5 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.4.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">6 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.5.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">7 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.6.tsv.jpg" style="width:100%">
  </div>

  <div class="mySlides">
    <div class="numbertext">8 / 8</div>
      <img src="/images/blog_images/kandinsky/arjun.papers.7.tsv.jpg" style="width:100%">
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>

  <!-- Image text -->
  <div class="caption-container">
    <p id="caption"></p>
  </div>

  <!-- Thumbnail images -->
  <div class="row">
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.0.tsv.jpg" style="width:100%" onclick="currentSlide(1)" alt="Lauterber et al 2022">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.1.tsv.jpg" style="width:100%" onclick="currentSlide(2)" alt="Biddanda et al 2022">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.2.tsv.jpg" style="width:100%" onclick="currentSlide(3)" alt="Zhang et al 2022">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.3.tsv.jpg" style="width:100%" onclick="currentSlide(4)" alt="Biddanda et al 2022">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.4.tsv.jpg" style="width:100%" onclick="currentSlide(5)" alt="Biddanda et al 2020">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.5.tsv.jpg" style="width:100%" onclick="currentSlide(6)" alt="Damgaard et al 2018">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.6.tsv.jpg" style="width:100%" onclick="currentSlide(7)" alt="Chiang et al 2018">
    </div>
    <div class="column">
      <img class="demo cursor" src="/images/blog_images/kandinsky/arjun.papers.7.tsv.jpg" style="width:100%" onclick="currentSlide(7)" alt="Waldman et al 2016">
    </div>
  </div>
</div>

