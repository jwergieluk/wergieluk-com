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

A Python package is just a file, so a simple package repository 

One of my packages, `signaldb`, employs the usual `setup.py` script generating
`signaldb-x.y.z.whl` package file. Instead of using a Makefile for calling the
build script and deploying the wheel, I wrote the following 3 lines-long bash
equivalent generating and copying the wheel to the "repository" located
at `$local_pypi`. `$local_pypi` is conveniently defined in my `.profile` and
points to `~/packages`.

````
#!/bin/bash

set -e; set -u

python setup.py bdist_wheel
cp dist/*.whl ${local_pypi}
````

The easiest way to install `signaldb` package with `pip` is to specify the wheel file
explicitly:

    pip install ${local_pypi}/signaldb-0.0.1.whl

It is also possible to install the package just by saying

    pip install signaldb

For that, we first need to inform `pip` where to look for the package: An additional
repository supplementing `pypi.python.org` can be specified with
    
    pip install --extra-index-url "file://${local_pypi}/"

or by exporting an env variable

    export PIP_EXTRA_INDEX_URL="file://${local_pypi}/"

This alone won't work though. The PyPI repository needs to obey the [PEP
503](https://www.python.org/dev/peps/pep-0503/): Each package must reside in
its own subdirectory named after the package, and repo root must contain an
`index.html` with links to the package files. 

Luckly, there is a Python tool called
[pip2pi](https://github.com/wolever/pip2pi) that can convert our bunch of
wheels into a property stuctured repository with index files. `pip2pi` exposes
a command-line utility `dir2pi` generating a proper PyPI repository in the
subdirectory `simple` of a directory specified in the argument:

    dir2pi -n ${local_pypi}

In our case we get 

```
packages/simple/index.html
packages/simple/signaldb
packages/simple/signaldb/signaldb-0.0.1-py3-none-any.whl
packages/simple/signaldb/signaldb-0.0.2-py3-none-any.whl
packages/simple/signaldb/index.html

```

Finally, we need to update `.profile` or `.bashrc`:

    export PIP_EXTRA_INDEX_URL="file://${local_pypi}/simple/"

which allows for
```
$ pip install signaldb
Collecting signaldb
[...]
Successfully installed signaldb-0.0.2 [...]
```

## Conclusion

The outlined method shows that a simple private PyPI repository does not
require a server component. Such a repository can handle multiple package
versions and can easily be synchronized amongn multiple machines using tools
like `syncthing` or similar.

## References

* [pip2pi](https://github.com/wolever/pip2pi).
* [PEP 503](https://www.python.org/dev/peps/pep-0503/) -- Simple Repository API.



<!-- vim: spelllang=en_us:spell: -->
