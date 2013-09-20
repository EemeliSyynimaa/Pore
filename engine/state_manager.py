__author__ = 'eeneku'

import states


class StateManager(object):
    """ This class handles the states in the game. """

    def __init__(self, engine):
        self.engine = engine
        self.main_states = states.main_states
        self.states = {}
        self.active_states = []

    def add(self, name, state):
        self.states[name] = state
        
    def activate(self, state, *args, **kwargs):
        if state in self.main_states:
            for active_state in self.active_states:
                active_state.cleanup()
                self.engine.remove_handlers(active_state)
                # TODO: SEE IF IT WORKS
                
            self.active_states = []
            self.states = {}

            for st in self.main_states[state].states:
                self.states[st] = self.main_states[state].states[st]

            self.active_states.append(self.states[self.main_states[state].enter_state](self, *args, **kwargs))
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
    
    def draw(self):
        for scene in self.active_states:
            scene.draw()