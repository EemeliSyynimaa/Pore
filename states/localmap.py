__author__ = 'eeneku'

from pyglet.window import key

from engine import state

class LocalMap(state.State):
    """ The local map state. """

    def __init__(self, manager):
        super(LocalMap, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            print("end of line!")
            print(self.manager.active_states)
            self.manager.change("main_menu")
        elif symbol == key.S:
            print("local_map > world_map")
            self.manager.pop()

    def on_draw(self):
        self.batch.draw()
