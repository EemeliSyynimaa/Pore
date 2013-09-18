from pyglet import sprite

class Sprite(sprite.Sprite):
    """ A traditional Sprite class. """

    def __init__(self, *args, **kwargs):
        super(Sprite, self).__init__(*args, **kwargs)