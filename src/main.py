#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import engine

# Import scenes
from scenes import game

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 720
        
        self.engine = engine.Engine(width=self.screen_w, 
                                    height=self.screen_h,
                                    fullscreen=False)
        
        self.init_resources()
        self.init_scenes()
        
        self.engine.run()
        
    def init_resources(self):
        self.engine.add_resource_path('gfx')
        
    def init_scenes(self):
        self.engine.scene_manager.add_scene('game', game.Game)
        self.engine.scene_manager.activate_scene('game', self.screen_w,
                                                 self.screen_h)

        
        
if __name__ == '__main__':
    app = App()  