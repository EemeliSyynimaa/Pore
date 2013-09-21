# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from engine import state

from game import tile_map


class WorldMap(state.State):
    """
    The world map state.
    """

    def __init__(self, manager):
        super(WorldMap, self).__init__(manager)
        self.init_resources()

        self.tile_map = tile_map.TileMap()
        self.tile_map.load('test_map.json')
        self.tile_map.set_view(320, 40, 640, 640)
        self.tile_map.update()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_draw(self):
        self.batch.draw()
        self.tile_map.draw()
