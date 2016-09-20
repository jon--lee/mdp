"""
    Interface for discrete environment (such as farm)
"""

class DiscreteEnv():

    def __init__(self):
        raise NotImplementedError


    def is_valid(self, state):
        # determine whether a state is valid (i.e)
        raise NotImplementedError
        
    def reset_mdp(self)
        # reset mdp to initial state
        # reset any environment settings
        raise NotImplementedError

    def transition_prob(self, state, action, next_state):
        # Constraint: [sum_{s'} T(s, a, s')] = 1
        # could be deterministic
        raise NotImplementedError

    def get_adjacent(self, state):
        # list of states that are within one action of state (i.e. neighbors)
        raise NotImplementedError

    def reward(self, state, action, next_state):
        # Could just depend on next_state
        # return negative/positive real number
        raise NotImplementedError


    def update_mdp(self, action):
        # given aciton from mdp, update state to some next_state
        raise NotImplementedError
    

        
    
