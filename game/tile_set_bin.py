# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import game.tile


class TileSetBin(object):
    """
    This class holds images of all tiles in tile set.
    """
    def __init__(self):
        self.tiles = []

    def add(self, image, type):
        self.tiles.append(game.tile.Tile(image.get_texture(), type))

    def get_tile_type(self, gid):
        return self.tiles[gid].type

    def get_tex_coords(self, gid):
        return self.tiles[gid].texture.tex_coords

    def get_texture(self, gid):
        return self.tiles[gid].texture.texture