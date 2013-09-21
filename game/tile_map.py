# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import pyglet
import math
import json

import game.layer
import game.tile
import game.tile_set_bin


class TileMap(object):
    """
    This class holds all tile layers in one map.
    """

    def __init__(self):
        self.layers = []

        self.tile_width = 0
        self.tile_height = 0

        self.width = 0
        self.height = 0

        self.version = ""
        self.orientation = ""
        self.properties = {}

        self.tile_set_bin = None

        self.batch = None

        self.view_x = 0
        self.view_y = 0
        self.view_width = 0
        self.view_height = 0

        self.world_x = 0
        self.world_y = 0

    def set_view(self, x, y, width, height):
        self.view_x = x
        self.view_y = y
        self.view_width = width
        self.view_height = height

    def update_view(self):
        self.batch = pyglet.graphics.Batch()

        for y in range(self.height):
            y1 = self.view_y + (self.height*self.tile_height) - (self.tile_height * y)
            y2 = y1 - self.tile_height

            for x in range(self.width):
                x1 = self.view_x + self.tile_width * x
                x2 = x1 + self.tile_width

                for layer in reversed(self.layers):
                    if layer.type == 'tilelayer' and (x, y) in layer.data:
                        gid = layer.get_gid((x, y))
                        self.batch.add(4,
                                       pyglet.gl.GL_QUADS,
                                       pyglet.graphics.TextureGroup(self.tile_set_bin.get_texture(gid)),
                       ('v2i', [x1, y2, x2, y2, x2, y1, x1, y1]),
                       ('t3f', self.tile_set_bin.get_tex_coords(gid)),
                       ('c4B', (255, 255, 255, 255)*4))

    def draw(self):
        self.batch.draw()

    def load(self, path):
        with open(path) as map_file:
            map_data = json.load(map_file)

        self._load_layers(map_data)
        self._load_attributes(map_data)
        self._load_properties(map_data)
        self._load_tile_sets(map_data)

    def _load_layers(self, map_data):
        for layer in map_data['layers']:
            self._add_new_layer(layer)

    def _add_new_layer(self, layer):
        new_layer = game.layer.Layer()

        new_layer.type = layer['type']
        new_layer.width = layer['width']
        new_layer.height = layer['height']
        new_layer.name = layer['name']

        if new_layer.type == 'tilelayer':
            self._load_layer_tiles(new_layer, layer['data'])
        elif new_layer.type == 'objectgroup':
            self._load_layer_objects(new_layer, layer['objects'])

        self.layers.append(new_layer)

    def _load_layer_tiles(self, new_layer,  layer_data):
        new_layer.data = {}

        assert len(layer_data) == new_layer.width * new_layer.height

        i = 0

        for row in range(new_layer.width):
            for col in range(new_layer.width):
                if layer_data[i] < 1:
                    continue

                new_layer.data[(col, row)] = game.tile.Tile(layer_data[i]-1)

                i += 1

    def _load_layer_objects(self, new_layer, layer):
        new_layer.data = layer

    def _load_attributes(self, map_data):
        self.tile_width = map_data['tilewidth']
        self.tile_height = map_data['tileheight']
        self.version = map_data['version']
        self.width = map_data['width']
        self.height = map_data['height']
        self.orientation = map_data['orientation']

    def _load_properties(self, map_data):
        if 'properties' in map_data:
            for key in map_data['properties']:
                self.properties[key] = map_data['properties'][key]

    def _load_tile_sets(self, map_data):
        tiles = []

        for tile_set in map_data['tilesets']:
            tiles.extend(self._load_tiles(tile_set))

        self._add_tiles_to_bin(tiles)

    def _load_tiles(self, tile_set):
        tiles = []

        # TODO: build a wrapper (or something) for this image load
        image = pyglet.image.load(tile_set['image'])
        tiles_width = image.width / self.tile_width
        tiles_height = image.height / self.tile_height

        for row in range(tiles_height):
            for col in range(tiles_width):
                tiles.append(image.get_region(col*self.tile_width,
                                              (image.height-self.tile_height)-row*self.tile_height,
                                              self.tile_width,
                                              self.tile_height))

        return tiles

    def _add_tiles_to_bin(self, tiles):
        self.tile_set_bin = game.tile_set_bin.TileSetBin()

        for tile in tiles:
            self.tile_set_bin.add(tile)