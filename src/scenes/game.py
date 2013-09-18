# -*- coding: utf-8 -*-

from engine import scene

import tilemap

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager, screen_w, screen_h):
        super(Game, self).__init__(manager)
        
        self.screen_w = screen_w
        self.screen_h = screen_h
        
        self.init_resources()
        
        self.map = tilemap.TileMap(0, screen_h-16, self.res, self.batch)
        
    def init_resources(self):
        self.res.load_image("grass.png")
    
    def update(self, dt):
        pass
            
    def on_draw(self):
        self.batch.draw()
