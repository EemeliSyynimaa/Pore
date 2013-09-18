# -*- coding: utf-8 -*-

from pyglet.text import Label


class Label(Label):
    """ A wrapper class for pyglet.text.Label """

    def __init__(self, *args, **kwargs):
        super(Label, self).__init__(*args, **kwargs)
        