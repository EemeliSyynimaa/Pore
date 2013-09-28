# -*- coding: utf-8 -*-
__author__ = 'eeneku'


class Tile(object):
    """
    This class stores data of one tile in tile set.
    """

    def __init__(self, texture, properties):
        self.texture = texture
        self.properties = properties