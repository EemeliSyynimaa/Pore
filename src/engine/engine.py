# -*- coding: utf-8 -*-

import pyglet

import scene_manager

class Engine(pyglet.window.Window):
    """ The main engine class. """
    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        
        self.scene_manager = scene_manager.SceneManager(engine=self)
        self.fps = pyglet.clock.ClockDisplay()
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)
    
    def update(self, dt):
        self.scene_manager.update(dt)
    
    def run(self):
        pyglet.app.run()
        
    def draw(self):
        self.clear()
        self.scene_manager.draw()
        self.fps.draw()