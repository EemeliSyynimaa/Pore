__author__ = 'eeneku'

from engine import scene


class WorldMap(scene.Scene):
    """ The World Map scene. """

    def __init__(self, manager, screen_w, screen_h):
        super(WorldMap, self).__init__(manager)

        self.screen_w = screen_w
        self.screen_h = screen_h

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.batch.draw()
