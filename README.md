# clibs
Cython bindings for selected C libraries.

## glfw3

### Installation

On Linux or OSX, install builds from your favourite package manager, e.g. [Homebrew](http://brew.sh/):
```
brew install glfw3
```

Install bindings with the provided setup script:
```
python setup.py install clibs.glfw3
```

### Usage

```python
from clibs import glfw3

def handle_keyboard_key(window, key, scancode, action, mods):
    if key == glfw3.GLFW_KEY_ESCAPE and action == glfw3.GLFW_RELEASE:
        window.should_close = True

with glfw3.initialized():
    window = glfw3.Window("Hello GLFW3!", (800, 600))
    
    window.on_keyboard_key(handle_keyboard_key)
    
    context = glfw3.Context(window)
    glfw3.Context.set_current(context)

    while not window.should_close():
        glfw3.poll_events()
        
        # OpenGL Code
        
        window.swap_buffers()
```

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
from clibs import mcpp

p = mcpp.Preprocessor()
print(p.preprocess('-P', 'path/to/header.h'))
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
python setup.py install clibs.tess2
```

### Usage

```python
from clibs import tess2

t = tess2.Tesselator()
t.add_contour([[1.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, -1.0, 0.0], [1.0, -1.0, 0.0]])
t.tesselate(TESS_WINDING_ODD, TESS_POLYGONS)
print(list(t))
```