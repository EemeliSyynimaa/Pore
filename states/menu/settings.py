__author__ = 'eeneku'

from engine import state


class Settings(state.State):
    """ The settings state. """

    def __init__(self, manager):
        super(Settings, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.batch.draw()
