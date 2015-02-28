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

glfw3_lib = 'glfw3'
mcpp_lib = 'mcpp'
tess2_lib = 'tess2'

platform = sys.platform.lower()
if 'darwin' in platform or 'linux' in platform:
    extra_compile_args.extend(['-I/usr/local/include', '-I/opt/local/include'])
    extra_link_args.extend(['-L/usr/local/lib', '-L/opt/local/lib'])

if 'win32' in platform:
    glfw3_lib = 'glfw3dll'
    glfw3_root = os.environ.get('GLFW_ROOT')
    extra_compile_args.append('-I%s' % (os.path.join(glfw3_root, 'include'),))
    extra_link_args.append('/LIBPATH:%s' % (os.path.join(glfw3_root, 'lib-vc2013'),))

_all_ = {
    'clibs.glfw3': Extension('clibs.glfw3.glfw3', ['clibs/glfw3/glfw3.pyx'], libraries=[glfw3_lib],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    ),
    'clibs.mcpp': Extension('clibs.mcpp.mcpp_lib', ['clibs/mcpp/mcpp_lib.pyx'], libraries=[mcpp_lib],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    ),
    'clibs.openal': Extension('clibs.openal.al', ['clibs/openal/al.pyx'], libraries=[],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args + ['-framework', 'OpenAL']
    ),
    'clibs.opengl': Extension('clibs.opengl.gl3', ['clibs/opengl/gl3.pyx'], libraries=[],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args + ['-framework', 'OpenGL']
    ),
    'clibs.tess2': Extension('clibs.tess2.tesselator', ['clibs/tess2/tesselator.pyx'], libraries=[tess2_lib],
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
    ext_modules=ext_modules,
    zip_safe=True
)