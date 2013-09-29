# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from pyglet import sprite


class Entity(sprite.Sprite):
    """
    Entity class.
    """

    def __init__(self, *args, **kwargs):
        super(Entity, self).__init__(*args, **kwargs)

        self.move_x = 0
        self.move_y = 0

        self.target_x = 0
        self.target_y = 0

        self.move_speed = 0

        self.dialog = 'test'

