from .env_base import Environment


class Env4InRow(Environment):
    """
    An environment representing a 4-in-row game.
    Args:
        player1, player2: the players
        board_size (tuple): the size of the board.
    """
    def __init__(self, player1, player2, board_size):
        super(Env4InRow, self).__init__(player1, player2)
        # TODO - implement everything!

    def reset(self):
        pass

    def apply_action(self, player, action):
        pass

    def render(self):
        pass

    def available_moves(self, player):
        pass

    def is_terminal_state(self):
        pass

    def player_status(self, player):
        pass
