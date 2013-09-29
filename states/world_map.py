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

        self.groups = []

        self.player_group = entity.Entity(self.r_data.res.data['img_wizard'],
                                          x=224, y=160, batch=self.batch)

        self.groups.append(self.player_group)

        self.number_of_groups = random.randint(1, 20)
        self.init_npc_groups()

        self.label = Label('oo!', x=0, y=0)

        self.mouse_x = 0
        self.mouse_y = 0

        self.moving = False

        self.move_speed = 0.375

    def init_resources(self):
        self.r_data.res.load_image('img_wizard', 'wizard.png')
        self.r_data.res.load_image('img_orc', 'orc.png')

    def init_npc_groups(self):
        for i in range(self.number_of_groups):
            new_group = entity.Entity(img=self.r_data.res.data[random.choice(['img_wizard', 'img_orc'])],
                                      batch=self.batch)

            new_group.x = random.randint(0, self.tile_map.tile_width) * self.tile_map.tile_width
            new_group.y = random.randint(0, self.tile_map.tile_height) * self.tile_map.tile_height

            while not self.tile_map.has_tile_property((new_group.x, new_group.y), 'floor', 0) and \
                    not self.is_location_free((new_group.x, new_group.y)):
                new_group.x = random.randint(0, self.tile_map.tile_width) * self.tile_map.tile_width
                new_group.y = random.randint(0, self.tile_map.tile_height) * self.tile_map.tile_height

            self.groups.append(new_group)

    def is_location_free(self, (x, y)):
        for group in self.groups:
            if group.x == x and group.y == y:
                return group

    def handle_collision(self, (group_1, group_2)):
        dialog = __import__("dialog", fromlist=[group_1.dialog])
        dialog.__dict__[group_1.dialog].say_something()

    def check_collisions(self):
        for i in xrange(len(self.groups)):
            for j in xrange(i+1, len(self.groups)):
                if self.groups[i].x == self.groups[j].x and self.groups[i].y == self.groups[j].y:
                    self.handle_collision((self.groups[i], self.groups[j]))

    def move_groups(self, (x, y)):
        self.moving = True

        for group in self.groups:
            if group == self.player_group:
                new_x = x
                new_y = y
            else:
                new_x = random.choice([1, 0, -1])
                if new_x == 0:
                    new_y = random.choice([1, 0, -1])
                else:
                    new_y = 0

            new_target_y = group.y + new_y * self.tile_map.tile_height
            new_target_x = group.x + new_x * self.tile_map.tile_width

            if self.tile_map.has_tile_property((new_target_x, new_target_y), 'floor', 0):
                group.move_x = new_x
                group.move_y = new_y

                group.target_x = new_target_x
                group.target_y = new_target_y

                if new_x != 0:
                    group.move_speed = self.tile_map.tile_width / self.move_speed
                elif new_y != 0:
                    group.move_speed = self.tile_map.tile_height / self.move_speed
            else:
                group.move_x = 0
                group.move_y = 0
                group.move_speed = 0

        clock.schedule_once(self.stop_moving, self.move_speed)

    def stop_moving(self, dt):
        self.moving = False

        for group in self.groups:
            if group.move_speed > 0:
                group.x = group.target_x
                group.y = group.target_y

        self.check_collisions()

    def apply_movements(self, dt):
        for group in self.groups:
            group.x += group.move_x * group.move_speed * dt
            group.y += group.move_y * group.move_speed * dt

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
                self.move_groups((0, 1))
            elif self.engine.keys[key.S]:
                self.move_groups((0, -1))
            elif self.engine.keys[key.A]:
                self.move_groups((-1, 0))
            elif self.engine.keys[key.D]:
                self.move_groups((1, 0))
        else:
            self.apply_movements(dt)

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