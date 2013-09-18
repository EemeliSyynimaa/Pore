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
        
    def add_resource_path(self, location):
        pyglet.resource.path.append(location)
        pyglet.resource.reindex()
    
    def update(self, dt):
        self.scene_manager.update(dt)
    
    def run(self):
        pyglet.app.run()
        
    def on_draw(self):
        self.clear()
        self.scene_manager.on_draw()
        self.fps.draw()