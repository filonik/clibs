#! /usr/bin/python2

from __future__ import absolute_import, division, print_function

import os
import sys

from clibs import glfw3, opengl

def handle_keyboard_key(window, key, scancode, action, mods):
    if key == glfw3.GLFW_KEY_ESCAPE and action == glfw3.GLFW_RELEASE:
        window.should_close = True

def main():
    with glfw3.initialized():
        window = glfw3.Window("Hello GLFW3!", (800, 600))
        
        window.on_keyboard_key(handle_keyboard_key)
        
        glfw3.Context.set_current(window.context)

        while not window.should_close:
            glfw3.poll_events()
            
            opengl.clear([1,0,0])
            
            window.swap_buffers()

    return 0

if __name__ == "__main__":
    sys.exit(main())