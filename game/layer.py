# -*- coding: utf-8 -*-
__author__ = 'eeneku'


class Layer(object):
    """
    This class represents one layer in map.
    """

    def __init__(self):
        self.width = 0
        self.height = 0
        self.name = ""
        self.type = ""
        self.opacity = 0
        self.visible = True
        self.x = 0
        self.y = 0
        self.data = None

    def get_gid(self, key):
        if self.type == 'tilelayer':
            return self.data[key].gid