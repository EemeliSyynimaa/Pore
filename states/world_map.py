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

        self.move_speed = 0.25

    def init_resources(self):
        self.r_data.res.load_image('img_wizard', 'wizard.png')
        self.r_data.res.load_image('img_orc', 'orc.png')

    def move_entities(self, (x, y)):
        self.moving = True

        for entity in self.entities:
            if entity == self.entity_player:
                t_x = x
                t_y = y
            else:
                t_x = random.choice([1, 0, -1])
                if t_x == 0:
                    t_y = random.choice([1, 0, -1])
                else:
                    t_y = 0

            entity.move_x = t_x
            entity.move_y = t_y

            entity.target_y = entity.y + t_y * self.tile_map.tile_height
            entity.target_x = entity.x + t_x * self.tile_map.tile_width

            if t_x != 0:
                entity.move_speed = self.tile_map.tile_width / self.move_speed
            elif t_y != 0:
                entity.move_speed = self.tile_map.tile_height / self.move_speed

        clock.schedule_once(self.stop_moving, self.move_speed)

    def stop_moving(self, dt):
        self.moving = False

        for entity in self.entities:
            entity.x = entity.target_x
            entity.y = entity.target_y

    def make_movements(self, dt):
        for entity in self.entities:
            entity.x += entity.move_x * entity.move_speed * dt
            entity.y += entity.move_y * entity.move_speed * dt

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