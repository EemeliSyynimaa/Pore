# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import random

from pyglet.window import key
from pyglet import gl
from pyglet.text import Label
from pyglet import clock

from engine import state
from game import tile_map
from game import entity


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

        self.entities = []

        self.entity_player = entity.Entity(self.r_data.res.data['img_wizard'],
                                           x=224, y=160, batch=self.batch)
        self.entity_1 = entity.Entity(self.r_data.res.data['img_orc'],
                                      x=352, y=224, batch=self.batch)
        self.entity_2 = entity.Entity(self.r_data.res.data['img_orc'],
                                      x=320, y=192, batch=self.batch)

        self.entities.extend([self.entity_player, self.entity_1, self.entity_2])

        self.label = Label('oo!', x=0, y=0)

        self.mouse_x = 0
        self.mouse_y = 0

        self.moving = False

        self.move_speed = 0.375

    def init_resources(self):
        self.r_data.res.load_image('img_wizard', 'wizard.png')
        self.r_data.res.load_image('img_orc', 'orc.png')

    def move_entities(self, (x, y)):
        self.moving = True

        for ent in self.entities:
            if ent == self.entity_player:
                new_x = x
                new_y = y
            else:
                new_x = random.choice([1, 0, -1])
                if new_x == 0:
                    new_y = random.choice([1, 0, -1])
                else:
                    new_y = 0

            new_target_y = ent.y + new_y * self.tile_map.tile_height
            new_target_x = ent.x + new_x * self.tile_map.tile_width

            if self.tile_map.has_tile_property((new_target_x, new_target_y), 'floor', 0):
                ent.move_x = new_x
                ent.move_y = new_y

                ent.target_x = new_target_x
                ent.target_y = new_target_y

                if new_x != 0:
                    ent.move_speed = self.tile_map.tile_width / self.move_speed
                elif new_y != 0:
                    ent.move_speed = self.tile_map.tile_height / self.move_speed
            else:
                ent.move_x = 0
                ent.move_y = 0
                ent.move_speed = 0

        clock.schedule_once(self.stop_moving, self.move_speed)

    def stop_moving(self, dt):
        self.moving = False

        for ent in self.entities:
            if ent.move_speed > 0:
                ent.x = ent.target_x
                ent.y = ent.target_y

    def make_movements(self, dt):
        for ent in self.entities:
            ent.x += ent.move_x * ent.move_speed * dt
            ent.y += ent.move_y * ent.move_speed * dt

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

        if not self.moving:
            if self.engine.keys[key.W]:
                self.move_entities((0, 1))
            elif self.engine.keys[key.S]:
                self.move_entities((0, -1))
            elif self.engine.keys[key.A]:
                self.move_entities((-1, 0))
            elif self.engine.keys[key.D]:
                self.move_entities((1, 0))
        else:
            self.make_movements(dt)

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