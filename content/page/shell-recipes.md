---
title: "Shell Recipes"
date: 2021-05-24T16:42:52+02:00
draft: false
---

### Print the first and some other file line using `paste`

Paste output from two subshells:

    paste <(head -1 data.csv | tr ',' '\n' ) <(cat data.csv | grep pattern | tr ',' '\n') | bat 

# Referecens

* https://www.datascienceatthecommandline.com

