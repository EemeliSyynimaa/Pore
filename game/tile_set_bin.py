# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import game.tile


class TileSetBin(object):
    """
    This class holds images of all tiles in tile set.
    """
    def __init__(self):
        self.tiles = []

    def add(self, image, properties={}):
        self.tiles.append(game.tile.Tile(image.get_texture(), properties))

    def get_tile_type(self, gid):
        if 'type' in self.tiles[gid].properties:
            return self.tiles[gid].properties['type']
        else:
            return None

    def get_tex_coords(self, gid):
        return self.tiles[gid].texture.tex_coords

    def get_texture(self, gid):
        return self.tiles[gid].texture.texture