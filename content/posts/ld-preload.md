---
title: "Loading custom shared libraries in Linux"
date: 2017-06-05
draft: false
tags:
    - linux
---

This post shows how to enforce loading custom shared libraries for a given
executable on a Linux system.

It turns out that even playing computer games on Linux can sometimes teach us
something useful.  The other day, an attempt to run Nuclear Throne on my Arch
Linux system produced the following error message. 

    $ ./runner 
    ./runner: error while loading shared libraries: libcrypto.so.1.0.0: cannot open shared object file: No such file or directory

A quick investigation reveals that the missing shared library `libcrypto.so` belongs to
the `openssl` package which was apparently upgraded to a newer version.

    $ pacman -Qo /usr/lib/libcrypto.so
    /usr/lib/libcrypto.so is owned by openssl 1.1.0.e-1

The executable `runner` we are trying to run depends on version 1.0.0 of `openssl`. 
This can be easly seen from the output of the `ldd` command:

    $ ldd runner 
	linux-gate.so.1 (0xf7726000)
	libstdc++.so.6 => /usr/lib32/libstdc++.so.6 (0xf755e000)
    [...]
	libcrypto.so.1.0.0 => not found
	libssl.so.1.0.0 => not found
    [...]

Obviously, it wouldn't be wise to downgrade the openssl package. However, it is
possible to provide the shared library loader with a list of `.so` files
using the `LD_PRELOAD` variable.

In my case this simple call solves the problem:

    LD_PRELOAD=/path/to/libcrypto.so:/path/to/libssl.so ./runner

The `LD_PRELOAD` list must contain absolute paths to the relevant .so files
since the original `runner` executable can call another executable sitting in
some directory different from the current.

<!-- vim: set syntax=markdown: set spelllang=en: set spell: -->
