# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import pyglet
import json

import game.layer
import game.tile_set_bin


class TextureGroup(pyglet.graphics.TextureGroup):
    def set_state(self):
        super(TextureGroup, self).set_state()

        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D,
                                  pyglet.gl.GL_TEXTURE_MAG_FILTER,
                                  pyglet.gl.GL_NEAREST)
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D,
                                  pyglet.gl.GL_TEXTURE_MIN_FILTER,
                                  pyglet.gl.GL_NEAREST)


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

    def draw_world(self):
        self.batch = pyglet.graphics.Batch()

        for y in range(self.height):
            y1 = self.view_y + int(self.world_y) + self.tile_height + self.tile_height * y
            y2 = y1 - self.tile_height

            for x in range(self.width):
                x1 = self.view_x + int(self.world_x) + self.tile_width * x
                x2 = x1 + self.tile_width

                for layer in reversed(self.layers):
                    if layer.type == 'tilelayer' and (x, y) in layer.data:
                        gid = layer.get_gid((x, y))

                        self.batch.add(4,
                                       pyglet.gl.GL_QUADS,
                                       TextureGroup(self.tile_set_bin.get_texture(gid)),
                                       ('v2i', [x1, y2, x2, y2, x2, y1, x1, y1]),
                                       ('t3f', self.tile_set_bin.get_tex_coords(gid)),
                                       ('c4B', (255, 255, 255, 255)*4))

    def get_tile_type(self, (x, y), layer):
        if x >= 0 and y >= 0 and x < self.width*self.tile_width and y < self.height*self.tile_height:
            return self.tile_set_bin.get_tile_type(self.layers[layer].get_gid((int(x/self.tile_width),
                                                                               int(y/self.tile_height))))
        else:
            return "Position out of bounds"

    def move_map(self, (x, y)):
        self.world_x += x
        self.world_y += y

        if self.world_x > 0:
            self.world_x = 0
        elif self.world_x < -(self.width*self.tile_width-self.view_width):
            self.world_x = -(self.width*self.tile_width-self.view_width)

        if self.world_y > 0:
            self.world_y = 0
        elif self.world_y < -(self.height*self.tile_height-self.view_height):
            self.world_y = -(self.height*self.tile_height-self.view_height)

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

                new_layer.data[(col, new_layer.height-1-row)] = layer_data[i]-1
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
        tile_set_properties = {}

        for tile_set in map_data['tilesets']:
            tiles.extend(self._load_tiles(tile_set))

            if 'tileproperties' in tile_set:
                tile_set_properties.update(self._load_tile_set_properties(tile_set['tileproperties']))

        self._add_tiles_to_bin(tiles, tile_set_properties)

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

    def _load_tile_set_properties(self, tile_set_properties):
        properties = {}

        for key in tile_set_properties:
            properties[int(key)] = tile_set_properties[key]

        return properties

    def _add_tiles_to_bin(self, tiles, tile_set_properties):
        self.tile_set_bin = game.tile_set_bin.TileSetBin()

        i = 0
        for tile in tiles:
            if i in tile_set_properties:
                self.tile_set_bin.add(tile, tile_set_properties[i]['type'])
            else:
                self.tile_set_bin.add(tile, '')

            i += 1