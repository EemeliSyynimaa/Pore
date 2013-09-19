# -*- coding: utf-8 -*-

import pyglet

from engine import scene


class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager, screen_w, screen_h):
        super(Game, self).__init__(manager)

        self.screen_w = screen_w
        self.screen_h = screen_h

        self.init_resources()
        
    def init_resources(self):
        self.manager.res.load_image("tile_grass", "grass.png")
    
    def update(self, dt):
        pass
            
    def draw(self):
        self.batch.draw()
        self.manager.res.data["tile_grass"].blit(0, 0)
