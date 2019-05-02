class Agent:
    def __init__(self, name: str):
        self.name = name

    def choose_action(self, env):
        """
        Chooses an action to take on the environment.
        Args:
            env (Environment): the environment on which to take an action
                based upon the observations.
        """
        raise NotImplementedError

    def __repr__(self):
        """
        Returns a pretty string representation of this object.
        DO NOT OVERRIDE THIS!
        """
        return "{0}({1}){2}".format(self.name, self.__class__.__name__,
                                    '\n' + self.extra_repr())

    def extra_repr(self):
        """
        Returns extra string representation of the current object.
        Any derived class may override this.
        """
        return ''
