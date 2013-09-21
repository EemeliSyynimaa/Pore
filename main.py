#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'eeneku'

from engine import engine

import states


class App(object):
    """
    The main class that ties everything together.
    """
    
    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 720
        
        self.engine = engine.Engine(width=self.screen_w, 
                                    height=self.screen_h,
                                    fullscreen=False)
        
        self.init_resources()
        self.init_states()
        
        self.engine.run()
        
    def init_resources(self):
        self.engine.add_resource_path('gfx')
        
    def init_states(self):
        self.engine.state_manager.add('world_map', states.WorldMap)
        self.engine.state_manager.add('main_menu', states.MainMenu)
        self.engine.state_manager.add('local_map', states.LocalMap)
        self.engine.state_manager.change('world_map')

if __name__ == '__main__':
    app = App()  