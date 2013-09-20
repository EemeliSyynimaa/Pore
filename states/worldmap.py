__author__ = 'eeneku'

from pyglet.window import key

from engine import state

class WorldMap(state.State):
    """ The world map state. """

    def __init__(self, manager):
        super(WorldMap, self).__init__(manager)
        self.init_resources()

    def init_resources(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            print("world_map > local_map")
            self.manager.push("local_map")
        elif symbol == key.S:
            print("world_map > main_menu")
            self.manager.pop()

    def on_draw(self):
        self.batch.draw()
