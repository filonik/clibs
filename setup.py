from __future__ import absolute_import, division, print_function

import os
import sys

from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    print("Could not import Cython. Install `cython` and rerun.")
    sys.exit(1)

extra_compile_args = []
extra_link_args = []

platform = sys.platform.lower()
if 'darwin' in platform or 'linux' in platform:
    extra_compile_args.extend(['-I/usr/local/include', '-I/opt/local/include'])
    extra_link_args.extend(['-L/usr/local/lib', '-L/opt/local/lib'])

_all_ = {
    'clibs.mcpp': Extension('clibs.mcpp.mcpp_lib', ['clibs/mcpp/mcpp_lib.pyx'], libraries=['mcpp'],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    ),
    'clibs.tess2': Extension('clibs.tess2.tesselator', ['clibs/tess2/tesselator.pyx'], libraries=['tess2'],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    ),
}

selection = [arg for arg in sys.argv if arg.startswith('clibs.')]

for arg in selection: sys.argv.remove(arg)

ext_modules = cythonize(filter(None, [_all_.get(arg) for arg in selection]))

setup(
    name="clibs",
    version = "0.0.1",
    license = 'MIT',
    author="Daniel Filonik",
    author_email="d.filonik@hdr.qut.edu.au",
    cmdclass={'build_ext': build_ext},
    packages=['clibs'] + selection,
    package_data={package: ['*.pyx', '*.pxd'] for package in selection},
    requires=['cython'],
    ext_modules=ext_modules
)