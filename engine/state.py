# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import pyglet


class State(object):
    """
    This class represents one state (screen) in the game.
    """

    def __init__(self, manager, engine):
        self.manager = manager
        self.engine = engine
        self.batch = pyglet.graphics.Batch()
        
    def on_key_press(self, symbol, modifiers):
        pass
    
    def on_key_release(self, symbol, modifiers):
        pass
        
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass 
    
    def on_mouse_enter(self, x, y):
        pass  
    
    def on_mouse_leave(self, x, y):
        pass 
    
    def on_mouse_motion(self, x, y, dx, dy):
        pass 
    
    def on_mouse_press(self, x, y, button, modifiers):
        pass 
    
    def on_mouse_release(self, x, y, button, modifiers):
        pass
     
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass 
    
    def on_text(self, text):
        pass
    
    def on_text_motion(self, motion):
        pass
    
    def on_text_motion_select(self, motion):
        pass
    
    def draw(self):
        pass
        
    def update(self, dt):
        pass
        
    def cleanup(self):
        pass