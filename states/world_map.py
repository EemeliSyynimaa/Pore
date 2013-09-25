# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from pyglet.window import key
from pyglet import gl
from pyglet import sprite
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

        self.entity_1 = entity.Entity(self.r_data.res.data['img_wizard'],
                                      x=224, y=160, batch=self.batch)
        self.entity_2 = entity.Entity(self.r_data.res.data['img_orc'],
                                      x=320, y=192, batch=self.batch)

        self.entities.extend([self.entity_1, self.entity_2])

        self.label = Label('oo!', x=0, y=0)

        self.mouse_x = 0
        self.mouse_y = 0

        self.moving = False

        self.entity_1.move_speed = 32
        self.move_speed = 0.5

    def init_resources(self):
        self.r_data.res.load_image('img_wizard', 'wizard.png')
        self.r_data.res.load_image('img_orc', 'orc.png')

    def move_entity(self, object, (x, y)):
        # TODO: Implement a proper moving system and a collision check system!
        # We should be moving one tile at a time, every unit at the same speed.
        # No need for fanciness. We just check if the tile we are moving to is free.
        self.moving = True

        object.move_x = x
        object.move_y = y
        object.target_x = object.x + x * self.tile_map.tile_width
        object.target_y = object.y + y * self.tile_map.tile_height

        if x != 0:
            object.move_speed = self.tile_map.tile_width / self.move_speed
        else:
            object.move_speed = self.tile_map.tile_height / self.move_speed

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
                self.move_entity(self.entity_1, (0, 1))
            elif self.engine.keys[key.S]:
                self.move_entity(self.entity_1, (0, -1))
            elif self.engine.keys[key.A]:
                self.move_entity(self.entity_1, (-1, 0))
            elif self.engine.keys[key.D]:
                self.move_entity(self.entity_1, (1, 0))
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