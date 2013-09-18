# -*- coding: utf-8 -*-

from pyglet.gl import *

def scale_image(image, width, height):
    image.get_texture()
    
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, 
                       gl.GL_NEAREST)
    
    image.width = width
    image.height = height
    
    return image
        
    