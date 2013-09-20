__author__ = 'eeneku'

from engine import state


class Intro(state.State):
    """ The intro state. """

    def __init__(self, manager):
        super(Intro, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.batch.draw()
