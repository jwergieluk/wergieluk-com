---
title: "Notes on migrating this blog to Hugo and Netlify"
date: 2018-10-03T18:33:56+02:00
draft: true
---

This is mainly for my own record. 

This is a static website generated using [Hugo](gohugo.io). The sources are 
hosted on GitHub and the compiled website is served by Netlify. I can also
use forestry.io to edit the content. The domain name is unfortunately still
with my old provider.

* Git repository hosted on GitHub: (https://github.com/jwergieluk/wergieluk-com)

Netlify monitors that repos and recompiles the site each time it see a commit. 

## DNS configuration -- domain provider

Unfortunately, my domain name provider (Domain Factory) doesn't support domain
name flattening.

    wergieluk.com 	A 	  	104.198.14.52
    www.wergieluk.com 	CNAME 	  	agitated-hodgkin-44.netlify.com

## Web-editor: forestry.io

... 




