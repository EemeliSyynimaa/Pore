# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from engine import state


class MainMenu(state.State):
    """
    The main menu state.
    """

    def __init__(self, manager):
        super(MainMenu, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_draw(self):
        self.batch.draw()