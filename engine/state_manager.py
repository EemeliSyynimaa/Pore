__author__ = 'eeneku'


class StateManager(object):
    """ This class handles the states in the game. """

    def __init__(self, engine):
        self.engine = engine
        self.states = {}
        self.active_states = []

    def add(self, name, state):
        self.states[name] = state
        
    def change(self, state, *args, **kwargs):
        if state in self.states:
            for active_state in self.active_states:
                active_state.cleanup()
                self.engine.remove_handlers(active_state)
                
            self.active_states = []

            self.active_states.append(self.states[state](self, *args, **kwargs))
            self.engine.push_handlers(self.active_states[-1])
            
    def push(self, state, *args, **kwargs):
        if state in self.states:
            if self.active_states:
                self.engine.pop_handlers()
                
            self.active_states.append(self.states[state](self, *args, **kwargs))
            self.engine.push_handlers(self.active_states[-1])

    def pop(self):
        if self.active_states:
            self.engine.pop_handlers()
            self.active_states.pop()
            
            if self.active_states:
                self.engine.push_handlers(self.active_states[-1])
        
    def update(self, dt):
        if self.active_states:
            self.active_states[-1].update(dt)
    
    def on_draw(self):
        for state in self.active_states:
            state.on_draw()