---
layout: post
title: "Shell Tricks (Grad School Year 1)"
description: "Shell functions for productivity"
categories: ["bash", "shell"]
---


Whenever you find yourself having to do something multiple times (e.g. copy a bunch of files at once) it is useful to have some shortcuts in the shell to be able to do a lot of these operations quickly. Here are a couple of my favorite little functions over the course of my first year in grad school that have helped me out.

### Compression Routines

In order to maintain some level of computer organization and directory structure it is useful to be able to identify which projects are "stalled" and are not actively being worked on. In addition, there are some directories that may contain long-term resources such as course notes or planning materials that you access very infrequently. If you have many of these directories (like me) it can quickly bloat your system or Dropbox. Here are couple of easy functions to help you compress those directories and save a bit of space in the process.   

{% highlight bash %}
#Usage: targz <directory>
targz (){
	dir=${1%/}
	tar -zcvf ${dir}.tar.gz $dir
}

alias untar='tar -xvf'

{% endhighlight %}


You could always use different flags for `tar` if you need to, but the vanilla version above gets you pretty far in having a nice function to compress those pesky directories that take up a lot of space and are not really doing a whole lot.

I also like to have photos from my travels stored on my Dropbox, but with the quality of modern smartphone cameras the photos quickly take up more and more space (~2 Mb per picture!). I was wondering how to compress these images (`*.jpg` in particular) and stumbled upon the tool `jpgoptim`, which you can install using `brew`.  I've really been enjoying this tool for making my photo albums more manageable.

{% highlight bash %}
#Usage : jpgzip <pct compressed>
jpgzip (){
  RATIO=$1
  jpegoptim -m${RATIO} *.jpg
}
{% endhighlight %}

Note that the compression that is used on the images here is "lossy" so the quality of the images is reduced to whatever percentage you want. With the "lossless" compression option of `jpgoptim` you roughly get compression ratios of < 5% but with the lossy version (depending on the parameter) you can get much much higher ratios. I find this particularly useful to compress my pictures in my Dropbox folders so it occupies a little less space on my laptop.

### System Checks

Having a macbook pro, sometimes plugging in `htop` is nice to be able to check the system and processes that are going on. However there are a couple of things that are generally nice to check, but are a little more elusive. The first is to be able to check your internet speed from within the terminal. You can use the function below to check it (it downloads an 10Mb file to `/dev/null`):

{% highlight bash %}

alias speedtest='curl -o /dev/null http://speedtest.sea01.softlayer.com/downloads/test10.zip'

{% endhighlight %}

*EDIT (9-10-2017)* : I would recommend using the [`speedtest-cli`](https://github.com/sivel/speedtest-cli) instead of the above function. It gives you much more information and is quite handy when dealing with cafe wifi.

One other thing that I have found nice from time to time is to check the battery health of my laptop (how many charge cycles it has gone through). This is a good indicator of [how long a laptop will last](https://support.apple.com/en-us/HT201585)

{% highlight bash%}

alias chkbat='system_profiler SPPowerDataType | grep "Cycle Count"'

{% endhighlight %}

Note that the above is only for Mac OS X, but I imagine there should be some Linux and Windows analogs of this function.


### Setting up Projects and TeX

One thing that I find myself doing fairly often is setting up directories for projects so that I have a couple of standard directories. This helps me avoid thinking too much about the initial directory structure and that way I can focus on writing the scripts and pipelines that I need to.

{% highlight bash%}
# Usage : setupproject <project_name>
setupproject(){
	mkdir $1
	touch $1/README.md
	echo -e "$1\n-------------------------------" > $1/README.md
	mkdir $1/data
	mkdir $1/src
	mkdir $1/plots
	mkdir $1/doc
}
{% endhighlight %}

Another thing that has helped is having a template from which to setup my python scripts, so that they all roughly follow the same general recipe using `argparse` and other libraries. To see the template file please see [here](https://gist.github.com/aabiddanda/d32a75e8f14b0e471ceb6ff3c625ef1b)

{% highlight bash %}
  # Sets up a canonical python script from a template
  setuppy(){ cp ~/.pytemplate $1}
{% endhighlight %}
