---
title: Notes on migrating this blog to Netlify and Hugo
date: 2018-10-03 16:33:56 +0000
lastmod: 2018-10-20
---

Written mainly for my own record.

This blog is a static website generated using [Hugo](gohugo.io). The sources
are hosted on GitHub and the website is compiled and served by static website
hosting service Netlify, which monitors the afermentioned git repo and
recompiles the site each time it sees a new commit.

The content can be added or modified using git
directly or via [forestry.io](https://www.forestry.io).
Forestry can access a GitHub (or GitLab) repo containing source files of a Hugo
project and commit content on user's behalf.

The domain name is unfortunately still with my old provider. 

## DNS configuration

Unfortunately, my domain name provider (Domain Factory) doesn't support domain
name flattening. I ended up implementing the setup described here:
[https://www.netlify.com/docs/custom-domains/#dns-configuration](https://www.netlify.com/docs/custom-domains/#dns-configuration
"https://www.netlify.com/docs/custom-domains/#dns-configuration")

The www subdomain points to my primary domain at Netlify while an "A" DNS entry
is used to point the APEX domain to Netlify's load balancer’s IP address. Apparently
this makes load balancing and regional content distribution more difficult.

    wergieluk.com	A	104.198.14.52
    www.wergieluk.com	CNAME	agitated-hodgkin-44.netlify.com

## Takeaways

So far I am very happy with Netlify. The setup was super smooth and everything
worked out-of-the-box.  They even automatically provisioned a free SSL
certificate from Let's Encrypt. The documentation is another strong point of
the offering:
[https://www.netlify.com/docs/](https://www.netlify.com/docs/ "https://www.netlify.com/docs/")

* Apparently it's better to use the good old www subdomain as the root: [https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/ "https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/")
* Hugo documentation is hard to understand and sometimes quite confusing. There
  is a very nice Hugo tutorial by Mike Dane available on YouTube:
  (https://www.youtube.com/watch?v=qtIqKaDlqXo&list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)
* In Hugo, setting `markup: "mmark"` and `katex: true` in the front matter of a
  document activates the rendering of LaTeX formulas.
  [Mmark](https://mmark.nl/) is an alternative markdown parser with a better
  support of inline math than the standard "blackfriday" parser.

## Links

* Website sources on GitHub: (https://github.com/jwergieluk/wergieluk-com)

<!-- vim: set syntax=markdown: set spelllang=en: set spell: -->
