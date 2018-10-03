---
title: Notes on migrating this blog to Hugo and Netlify
date: 2018-10-03 16:33:56 +0000

---
Written mainly for my own record.

This blog is a static website generated using [Hugo](gohugo.io). The sources are hosted on GitHub and the website is compiled and served by static website hosting service Netlify. I can also use forestry.io to edit the content. Forestry can access the GitHub repo and commit content on my behalf. The domain name is unfortunately still with my old provider.

* Git repository hosted on GitHub: (https://github.com/jwergieluk/wergieluk-com)

Netlify monitors that repo and recompiles the site each time it sees a new commit.

## DNS configuration

Unfortunately, my domain name provider (Domain Factory) doesn't support domain name flattening. I ended up implementing the  setup described here: [https://www.netlify.com/docs/custom-domains/#dns-configuration](https://www.netlify.com/docs/custom-domains/#dns-configuration "https://www.netlify.com/docs/custom-domains/#dns-configuration")

The www subdomain points to my primary domain at Netlify while an "A" DNS entry is used to point the APEX domain to Netlify's load balancer’s IP address. This is apparently not ideal.

    wergieluk.com	A	104.198.14.52
    www.wergieluk.com	CNAME	agitated-hodgkin-44.netlify.com

## Take awaits

* Netlify has some very nice documentation: [https://www.netlify.com/docs/](https://www.netlify.com/docs/ "https://www.netlify.com/docs/")
* Apparently it's better to use the good old www subdomain as the root: [https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/ "https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/")

## Todos

* Read Hugo docs
* Play around with forestry.io