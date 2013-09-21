# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from engine import state


class LocalMap(state.State):
    """
    The local map state.
    """

    def __init__(self, manager):
        super(LocalMap, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_draw(self):
        self.batch.draw()
