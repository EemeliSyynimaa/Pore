# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import pyglet

import state_manager


class Engine(pyglet.window.Window):
    """
    The main engine class.
    """

    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        
        self.state_manager = state_manager.StateManager(engine=self)
        self.fps = pyglet.clock.ClockDisplay()
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def add_resource_path(self, location):
        pyglet.resource.path.append(location)
        pyglet.resource.reindex()
    
    def update(self, dt):
        self.state_manager.update(dt)
    
    def run(self):
        pyglet.app.run()
        
    def on_draw(self):
        self.clear()
        self.state_manager.on_draw()
        self.fps.draw()