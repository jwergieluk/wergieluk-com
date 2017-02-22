Title: Local and static Python PyPI repository
Slug: local-static-pypi-repo
Date: 2017-02-18
Modified: 2017-02-19
Category: Blog
Author: Julian Wergieluk
Tags: python
Status: published

Suppose we want to have a private Python PyPI repository shared among the
development machines for the packages that our projects depend on. There is a
whole slew of solutions to that problem available on the Internet. Most of them
propose a quite complicated setup, typically involving a web server. There are
also companies offering package hosting. 

Does it have to be so complicated? After all, a Python package is just a file,
so a simple package repository should be a directory because this is the
canonical way of making files accessible on a UNIX system. 

In this article, I will show how to configure pip to use a directory as an
additional source of packages.

## The method

One of my Python packages, `signaldb`, employs the usual `setup.py` script to
generate `signaldb-x.y.z.whl` package files. Instead of using a Makefile to
call the build script and deploy the wheel (a kind of Python package), I wrote
the following 3 lines-long bash equivalent generating and copying the wheel to
a "repository" located at `$local_pypi`. The `$local_pypi` environmental
variable is conveniently defined in my `.profile` and points to `~/packages`
directory.

```
#!/bin/bash

set -e; set -u

python setup.py bdist_wheel
cp dist/*.whl ${local_pypi}
```

The easiest way to install `signaldb` package with pip is to specify the wheel file
explicitly:

    pip install ${local_pypi}/signaldb-0.0.1.whl

It is also possible to install the package just by typing

    pip install signaldb

For that, we first need to inform pip where to look for the package. An additional
repository supplementing `pypi.python.org` can be specified with
    
    pip install --extra-index-url "file://${local_pypi}/"

or, by exporting an environmental variable associated with that pip option:

    export PIP_EXTRA_INDEX_URL="file://${local_pypi}/"

This alone won't work, though. The PyPI repository needs to obey [PEP
503](https://www.python.org/dev/peps/pep-0503/): Each package must reside in
its own subdirectory named after the package, and the root directory of the
repository must contain an `index.html` file with links to the package files. 

Luckily, there is a Python tool called
[pip2pi](https://github.com/wolever/pip2pi) that can convert a directory
containing a bunch of wheel files into a properly structured PyPI repository.
`pip2pi` exposes the command-line utility `dir2pi` generating a PyPI repository
in the subdirectory `simple` of a directory specified in the argument:

    dir2pi -n ${local_pypi}

(the `-n` option normalizes the package names to conform with PEP 503)
In our case we get 

```
packages/simple/index.html
packages/simple/signaldb
packages/simple/signaldb/signaldb-0.0.1-py3-none-any.whl
packages/simple/signaldb/signaldb-0.0.2-py3-none-any.whl
packages/simple/signaldb/index.html

```

The above wheel files are just symlinks to the wheels from the source directory.
Finally, we need to update `.profile` or `.bashrc`

    export PIP_EXTRA_INDEX_URL="file://${local_pypi}/simple/"

and invoke pip in a familiar way:

```
$ pip install signaldb
Collecting signaldb
[...]
Successfully installed signaldb-0.0.2 [...]
```

## Conclusion

The outlined method shows that a simple private PyPI repository does not
require a server component. Such a repository can handle multiple package
versions and can easily be synchronized among multiple machines using tools
like `syncthing` or similar.

## References

* [pip2pi](https://github.com/wolever/pip2pi).
* [PEP 503](https://www.python.org/dev/peps/pep-0503/) -- Simple Repository API.

<!-- vim: set syntax=markdown: set spelllang=en: set spell: -->
