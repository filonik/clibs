
#
# This file is autogenerated.
#

cimport c_glfw3

	#
	# Supplements:
	#


cdef class VideoMode:
    cdef const c_glfw3.GLFWvidmode * _this
    
    @staticmethod
    cdef inline VideoMode fromthis(c_glfw3.GLFWvidmode * _this):
        cdef VideoMode result = VideoMode.__new__(VideoMode)
        result._this = _this
        return result
    
    @staticmethod
    cdef inline void swap(VideoMode self, VideoMode other):
        self._this, other._this = other._this, self._this

cdef class Monitor:
    cdef const c_glfw3.GLFWmonitor * _this

    @staticmethod
    cdef inline Monitor fromthis(c_glfw3.GLFWmonitor * _this):
        cdef Monitor result = Monitor.__new__(Monitor)
        result._this = _this
        return result
    
    @staticmethod
    cdef inline void swap(Monitor self, Monitor other):
        self._this, other._this = other._this, self._this

cdef class Cursor:
    cdef const c_glfw3.GLFWcursor * _this

    @staticmethod
    cdef inline Cursor fromthis(c_glfw3.GLFWcursor * _this):
        cdef Cursor result = Cursor.__new__(Cursor)
        result._this = _this
        return result
    
    @staticmethod
    cdef inline void swap(Cursor self, Cursor other):
        self._this, other._this = other._this, self._this

cdef class Image:
    cdef c_glfw3.GLFWimage * _this
    cdef unsigned char[:,:,::1] _data

cdef class GammaRamp:
    cdef const c_glfw3.GLFWgammaramp * _this
    
    @staticmethod
    cdef inline GammaRamp fromthis(c_glfw3.GLFWgammaramp * _this):
        cdef GammaRamp result = GammaRamp.__new__(GammaRamp)
        result._this = _this
        return result
    
    @staticmethod
    cdef inline void swap(GammaRamp self, GammaRamp other):
        self._this, other._this = other._this, self._this

cdef class Window:
    cdef const c_glfw3.GLFWwindow * _this
    
    @staticmethod
    cdef inline Window fromthis(c_glfw3.GLFWwindow * _this):
        cdef Window result = Window.__new__(Window)
        result._this = _this
        return result
    
    @staticmethod
    cdef inline void swap(Window self, Window other):
        self._this, other._this = other._this, self._this
    
    cdef inline void release(self):
        self._this = NULL
    
    @staticmethod
    cdef inline void default_hints():
        c_glfw3.glfwDefaultWindowHints()
    
    @staticmethod
    cdef inline void hint(int target, int hint):
        c_glfw3.glfwWindowHint(target, hint)
    
    cpdef set_window_position_callback(self, cbfun)
    cpdef set_window_size_callback(self, cbfun)
    cpdef set_window_close_callback(self, cbfun)
    cpdef set_window_refresh_callback(self, cbfun)
    cpdef set_window_focus_callback(self, cbfun)
    cpdef set_window_iconify_callback(self, cbfun)
    cpdef set_framebuffer_size_callback(self, cbfun)
    cpdef set_key_callback(self, cbfun)
    cpdef set_char_callback(self, cbfun)
    cpdef set_char_mods_callback(self, cbfun)
    cpdef set_mouse_button_callback(self, cbfun)
    cpdef set_cursor_position_callback(self, cbfun)
    cpdef set_cursor_enter_callback(self, cbfun)
    cpdef set_scroll_callback(self, cbfun)
    cpdef set_drop_callback(self, cbfun)
    
    cpdef get_attribute(self, int attrib)
    cpdef get_input_mode(self, int mode)
    cpdef set_input_mode(self, int mode, int value)
    
    cpdef iconify(self)
    cpdef restore(self)
    cpdef show(self)
    cpdef hide(self)
    cpdef swap_buffers(self)

cdef class Context:
    cdef const c_glfw3.GLFWwindow * _this

    @staticmethod
    cdef inline Context fromthis(c_glfw3.GLFWwindow * _this):
        cdef Context result = Context.__new__(Context)
        result._this = _this
        return result

    @staticmethod
    cdef inline void swap(Context self, Context other):
        self._this, other._this = other._this, self._this
