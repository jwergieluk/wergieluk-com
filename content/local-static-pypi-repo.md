Title: Local and static Python PyPI repository
Slug: local-static-pypi-repo
Date: 2017-02-18
Category: Blog
Author: Julian Wergieluk
Tags: python
Status: published

Suppose we want to have a private python PyPI repository shared among our
development machines for the packages that we are developing. There is a whole
slew of solutions to that problem available on the Internet. Most of them
propose a quite complicated setup typically involving a web server. There
are also companies offering package hosting. 

My `signaldb` package, a revolutionary market data system, has the
usual `setup.py` script that can be used to generate `signaldb-x.y.z.whl`
package file. Instead of using a Makefile for building the wheel, I wrote 
a 3 lines-long deployment
script, generating and copying the package to repository directory `~/packages/`
which I access through an environmental variable `$local_pypi`.

````
#!/bin/bash

set -e; set -u

python setup.py bdist_wheel
cp dist/*.whl ${local_pypi}
````

The easiest way to install `signaldb` with pip is to specify the wheel file
explicitly:

    pip install ${local_pypi}/signaldb-0.0.1.whl



<!-- :spelllang=en_us:spell: >
