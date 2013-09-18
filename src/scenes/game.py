# -*- coding: utf-8 -*-

from engine import scene

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager, screen_w, screen_h):
        super(Game, self).__init__(manager)

        self.screen_w = screen_w
        self.screen_h = screen_h
        
    def init_resources(self):
        pass
    
    def update(self, dt):
        pass
            
    def draw(self):
        self.batch.draw()
