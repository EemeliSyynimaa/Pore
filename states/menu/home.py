__author__ = 'eeneku'

from engine import state


class Home(state.State):
    """ The home (main menu) scene. """

    def __init__(self, manager):
        super(Home, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.batch.draw()
