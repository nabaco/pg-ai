from .agent_base import Agent
import random


class RandomAgent(Agent):
    """
    An agent that takes legal actions randomly.
    TODO - implement everything
    """
    def __init__(self, name):
        super(RandomAgent, self).__init__(name)

    def choose_action(self, env):
        pass
