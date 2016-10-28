Title: Hash Collisions with Pairs of Integers
Date: 2016-10-28 19:19:43
Tags: hashtables, tuples
Status: draft


The use of hashtables as a data structure is almost ubiquitous in its ease of implementation and use. I was concerned with finding a good way to store two positive integers (a tuple) for a hashtable. However, I only had a hash function for a single integer, so I wanted to search for a couple of ways to combine the two numbers into one. 

# Pairing Functions

A pairing function can be defined as a primitive recursive bijection. Now a bijection is fairly strict (since it requires that the function is one-to-one), so we will relax this assumption here. A primitive recursive (PR)function has a fairly strict definition in complexity theory, but for our purposes, we will use the fact that most of the normal number theory functions (e.g. addition, division, factorial) are PR.

I will compare a couple of functions (1) addition, (2) multiplication, and (3) the Cantor Pairing function. To save you a trip to Wikipedia, we will define the Cantor Pairing function as the following:

$$\pi(x,y) = \frac{(x+y+1)(x+y)}{2} + y$$

It is certainly possible to have many pairs of positive integers give the same results for some of these functions (e.g. 10 + 0 = 8 + 2), but we wanted to see how this might scale for very large integers. I was also curious to see the actual space in bits that each transformed value would take up. To perform this, I undertook the following small simulation study. 

# Simulations








# References + Source
















