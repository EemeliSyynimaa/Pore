# -*- coding: utf-8 -*-

from engine import sprite

class Tile(sprite.Sprite):
    """ This class represents a single tile in tilemap. """

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)
        pass
        