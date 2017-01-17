Title: Using spaced repetition
Slug: spaced-repetition
Date: 2016-12-24
Category: Blog
Author: Julian Wergieluk
Tags: learning, mathematics, programming
Summary: My thoughts on spaced repetition and it's uses for learning math


I would like to share my experiences using spaced repetition
for retaining knowledge from technical subjects like 
programming, mathematics.


## Anki usage statistics


## General observations

Human brain is not a hard drive. 

It is important to optimize the review time. Ideally, each
card should contain an atomic amount of information and should
be constructed in such a way that the answer can be recalled
in a split of a second. This requires a precise and succint 
formulation of the question with exhaustive list of assumptions. 

Make it personal.

Do you really need to memorize it? Gwerns 5 minutes rule. 

It is ok to delete cards. Our pernality, interests and career path are 
constantly evolving. Some information are simply becoming irrelevant 
in general or no longer relevant or interesing for us. Some
card may also prove difficult to memorize for various reasons. 


## Using in LaTeX for learning mathematical formulas

When I started using Anki I thought, I need the LaTeX 
support for mathematical formulas. At some point I would 
event come up with a system for converting beamer-slides 
to Anki cards. It turns out that most of the time LaTeX
is actully not necessarily and makes the process of
card creation tedious, complicated and error prone. 

Nowadays I tend to use a mixed "text mode" notation.

If LaTeX is needed to write down a formula, then that formula is probably to
complicated and can not be reliably memorized in that form. A conclusion is
that such a formula should be decomposed into meaningful parts each of which
can be put onto a separate card. 

#### Example: Density of the normal distribution

The probability density function of the normal distribution p(x) is
given by 

    p(x) = 1/2sqrt{ Pi } sigma exp( ((x-mu)/sigma)^2).

This is a moderately complicated formula, and first queston we need to ask
ourselfs is, do we even need to memorize this? After all, the formula along
with an excelent article about the normal distribution is available on
Wikipedia. 

Reasons for attempting to learn this are thus not rational. For example 

* We would like to call ourselfs a mathematician, a statistician or maybe
a probabilits and everybody with that title on the business card must 
be able to recall that formula even after having several shots of whisky.
* Braggin about it
* Intimidating others.

#### Categorizig cards

Many people come up with a complicated system of decks in order to attempt 
to categorize the learned material. Anki even allows us to create a deck
hierarchy using subdecks. 

In my opinion, this makes the process of card crafting and learning more 
complicated and offers no obvious benefits

## Heisig's system for learning Japanese characters

Why is it interesting: 

* Encourages creativity and comming up with own stories. 
* Emotional associations make remembering much easier. This requires
comming up with personal, bizzare and maybe event stupid sounding associations. 

## Why sharing decks doesn't make any sense

* Sharing card decks has a negative effect on the effectiveness of the deck.
  The idea that somebody else will be reading it stimies the creativity.  We
  are reluctant to use personal memories, bizzare associations and therefore we
  make our cards less effective. 


## References 

* [Spaced repetition](https://www.gwern.net/Spaced%20repetition), gwern.net, 2016. A very exhaustive 
discussion of the manifold aspects of SR with many refereces to papers and blogs.
* [How I use Anki to learn mathematics](http://lesswrong.com/r/discussion/lw/o8e/how_i_use_anki_to_learn_mathematics/), 
Lesswrong. 



