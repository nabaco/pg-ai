from .agent_base import Agent


class HumanAgent(Agent):
    """
    A user interface for playing the game -
    Renders the environment for the user to see and decide which action to take by letting
    the user choose the action.
    TODO - implement everything!
    """
    def __init__(self, name):
        super(HumanAgent, self).__init__(name)

    def choose_action(self, env):
        pass