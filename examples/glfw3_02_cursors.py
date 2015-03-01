#! /usr/bin/python2

from __future__ import absolute_import, division, print_function

import os
import sys

import OpenGL
from OpenGL.GL import *

import numpy as np

from clibs import glfw3

def handle_keyboard_key(window, key, scancode, action, mods):
    if key == glfw3.GLFW_KEY_ESCAPE and action == glfw3.GLFW_RELEASE:
        window.should_close = True

def make_cursor_image(width, height):
    pixels = [[(0, 255*(x/width), 255*(y/height), 255) for x in range(width)] for y in range(height)]
    return glfw3.Image(pixels)

def load_cursor_image(path):
    import PIL.Image
    pixels = np.array(PIL.Image.open(path).convert("RGBA"))
    return glfw3.Image(pixels)

def main():
    with glfw3.initialized():
        window = glfw3.Window("Hello GLFW3!", (800, 600))
        
        image = make_cursor_image(32, 32)
        #image = load_cursor_image('examples/image.png')
        cursor = glfw3.Cursor(image, image.width/2, image.height/2)
        window.cursor = cursor
        
        window.on_keyboard_key(handle_keyboard_key)
        
        glfw3.Context.set_current(window.context)

        while not window.should_close:
            glfw3.poll_events()
            
            glClearColor(0, 0, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            window.swap_buffers()

    return 0

if __name__ == "__main__":
    sys.exit(main())