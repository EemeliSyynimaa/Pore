# -*- coding: utf-8 -*-
__author__ = 'eeneku'

class TileSetBin(object):
    """
    This class holds images of all tiles in tile set.
    """
    def __init__(self):
        self.tiles = []

    def add(self, image):
        self.tiles.append(image.get_texture())

    def get_tex_coords(self, gid):
        return self.tiles[gid].tex_coords

    def get_texture(self, gid):
        return self.tiles[gid].texture