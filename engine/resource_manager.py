# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import yaml
import pyglet


class ResourceManager(object):
    """
    Class for managing resources.
    """

    def __init__(self):
        self.data = {}

    def load_image(self, id, image, location=None):
        if id not in self.data:
            if location:
                temp_loader = pyglet.resource.Loader(location)
                temp = temp_loader.image(image)
            else:
                temp = pyglet.resource.image(image)

            self.data[id] = temp
        else:
            print(id + " already loaded!")

    def load_media(self, id, media, location=None):
        if id not in self.data:
            if location:
                temp_loader = pyglet.resource.Loader(location)
                temp = temp_loader.media(media)
            else:
                temp = pyglet.resource.media(media)

            self.data[id] = temp
        else:
            print(id + " already loaded!")


    def load_yaml(self, id, file):
        pass