# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from pyglet.image.atlas import TextureAtlas


class TileSetBin(object):
    """
    This class holds images of all tiles in tile set.
    """
    def __init__(self, width=256, height=256):
        self.atlas = TextureAtlas(width, height)
        self.tiles = []

    def add(self, image):
        self.tiles.append(self.atlas.add(image))

    def get_tex_coords(self, gid):
        return self.tiles[gid].tex_coords

    def get_texture(self):
        return self.atlas.texture