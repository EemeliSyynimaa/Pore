# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from pyglet.window import key
from pyglet import gl
from pyglet import sprite
from pyglet.text import Label

from engine import state
from engine import resource_manager
from game import tile_map


class WorldMap(state.State):
    """
    The world map state.
    """

    def __init__(self, r_data, *args, **kwargs):
        super(WorldMap, self).__init__(*args, **kwargs)

        self.r_data = r_data

        self.init_resources()

        self.tile_map = tile_map.TileMap()
        self.tile_map.load('test_map.json')
        self.tile_map.draw_world()
        self.tile_map.set_view(0, 0, self.engine.width, self.engine.height)

        self.sprite_1 = sprite.Sprite(self.r_data.res.data['img_wizard'],
                                      x=224, y=160, batch=self.batch)
        self.sprite_2 = sprite.Sprite(self.r_data.res.data['img_orc'],
                                      x=320, y=400, batch=self.batch)

        self.label = Label('oo!', x=0, y=0)

        self.mouse_x = 0
        self.mouse_y = 0

    def init_resources(self):
        self.r_data.res.load_image('img_wizard', 'wizard.png')
        self.r_data.res.load_image('img_orc', 'orc.png')

    def move_object(self, object, (x, y)):
        # TODO: Implement a proper moving system and a collision check system!
        # We should be moving one tile at a time, every unit at the same speed.
        # No need for fanciness. We just check if the tile we are moving to is free.
        object.x += x
        object.y += y

    def update(self, dt):
        self.label.text = self.tile_map.get_tile_type((self.mouse_x-self.tile_map.world_x,
                                                       self.mouse_y-self.tile_map.world_y), 0) + " at pos " + \
                          str((int((self.mouse_x-self.tile_map.world_x)/self.tile_map.tile_width),
                               int((self.mouse_y-self.tile_map.world_y)/self.tile_map.tile_height)))

        if self.engine.keys[key.UP]:
            self.tile_map.move_map((0, -256*dt))
        if self.engine.keys[key.DOWN]:
            self.tile_map.move_map((0, 256*dt))
        if self.engine.keys[key.LEFT]:
            self.tile_map.move_map((256*dt, 0))
        if self.engine.keys[key.RIGHT]:
            self.tile_map.move_map((-256*dt, 0))

        if self.engine.keys[key.W]:
            self.move_object(self.sprite_1, (0, 128*dt))
        if self.engine.keys[key.S]:
            self.move_object(self.sprite_1, (0, -128*dt))
        if self.engine.keys[key.A]:
            self.move_object(self.sprite_1, (-128*dt, 0))
        if self.engine.keys[key.D]:
            self.move_object(self.sprite_1, (128*dt, 0))

    def on_key_press(self, symbol, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_draw(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.tile_map.world_x, self.tile_map.world_y, 0)
        self.tile_map.draw()
        self.batch.draw()
        gl.glPopMatrix()
        gl.glLoadIdentity()
        self.label.draw()