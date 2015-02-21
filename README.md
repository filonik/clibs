# clibs
Cython bindings for selected C libraries.

## mcpp 

Cython bindings for mcpp (Matsui's C Preprocessor).

### Installation

On Linux or OSX, install builds from your favourite package manager, e.g. [Homebrew](http://brew.sh/):
```
brew install mcpp
```

Install bindings with the provided setup script:
```
python setup.py install clibs.mcpp
```

### Usage

```python
import sys

from clibs.mcpp import *

def preprocess(*args):
    mcpp_use_mem_buffers(1)

    if mcpp_lib_main((sys.argv[0],) + args) != 0:
        raise RuntimeError(mcpp_get_mem_buffer(ERR))

    return mcpp_get_mem_buffer(OUT)

print(preprocess('-P', 'path/to/header.h'))
```

## libtess2 

Cython bindings for libtess2.

### Installation

On Linux or OSX, install builds from your favourite package manager, e.g. [Homebrew](http://brew.sh/):
```
brew install libtess2
```

Install bindings with the provided setup script:
```
python setup.py install clibs.mcpp
```

### Usage

```python
import sys

from clibs.tess2 import *

t = Tesselator()
t.add_contour([[1.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, -1.0, 0.0], [1.0, -1.0, 0.0]])
t.tesselate()
print([polygon for polygon in t]
```