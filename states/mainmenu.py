__author__ = 'eeneku'

from pyglet.window import key

from engine import state


class MainMenu(state.State):
    """ The main menu state. """

    def __init__(self, manager):
        super(MainMenu, self).__init__(manager)

        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            print("main_menu > world_map")
            self.manager.push('world_map')
        elif symbol == key.S:
            print("closing..")
            self.manager.pop()

    def on_draw(self):
        self.batch.draw()