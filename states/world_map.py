# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from pyglet.window import key
from pyglet import gl
from pyglet import sprite

from engine import state
from engine import resource_manager
from game import tile_map


class WorldMap(state.State):
    """
    The world map state.
    """

    def __init__(self, *args, **kwargs):
        super(WorldMap, self).__init__(*args, **kwargs)

        self.res = resource_manager.ResourceManager()

        self.init_resources()

        self.tile_map = tile_map.TileMap()
        self.tile_map.load('test_map.json')
        self.tile_map.set_view(320, 40, 640, 640)
        self.tile_map.update_view()

        self.sprite_1 = sprite.Sprite(self.res.data['img_wizard'],
                                      x=320, y=320, batch=self.batch)
        self.sprite_2 = sprite.Sprite(self.res.data['img_orc'],
                                      x=320, y=400, batch=self.batch)

    def init_resources(self):
        self.res.load_image('img_wizard', 'wizard.png')
        self.res.load_image('img_orc', 'orc.png')

    def update(self, dt):
        if self.engine.keys[key.UP]:
            self.sprite_2.y += 192 * dt
        if self.engine.keys[key.DOWN]:
            self.sprite_2.y -= 192 * dt
        if self.engine.keys[key.LEFT]:
            self.sprite_2.x -= 192 * dt
        if self.engine.keys[key.RIGHT]:
            self.sprite_2.x += 192 * dt

    def on_key_press(self, symbol, modifiers):
        pass

    def on_draw(self):
        self.tile_map.draw()
        self.batch.draw()
