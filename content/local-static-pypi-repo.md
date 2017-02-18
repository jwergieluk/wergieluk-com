Title: Local and static Python PyPI repository
Slug: local-static-pypi-repo
Date: 2017-02-18
Category: Blog
Author: Julian Wergieluk
Tags: python

Suppose we want to have a private python PyPI repository shared among our
development machines for the packages that we are developing. There is a whole
slew of solutions to that problem availble on the internet. Most of them
propose a quite complicated setup typically involving a web server.

My signaldb package, containg the revolutionary market data system, has the
usual `setup.py` script that can be used to generate `signaldb-0.0.1.whl`
package file. Instead of using a Makefile I have a 3 lines long deployment
script, generating and copying the wheel to repo directory `~/packages/` 
which I access through a environmental variable `$local_pypi`. 

````
#!/bin/bash

set -e; set -u

python setup.py bdist_wheel
cp dist/*.whl ${local_pypi}
dir2pi -n ${local_pypi} 
````

The easiest way to install signaldb with pip is to specify the package file explicitly:

    pip install ${local_pypi}/signaldb-0.0.1.whl


