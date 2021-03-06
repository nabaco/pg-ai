#!/usr/bin/env python3
from envs  import *
from agents import *

import pytest


class DummyAgent(Agent):
    def choose_action(self, env):
        pass


class TestEnv4InRow(object):
    def test_game(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 4
        height = 2
        game = create_env('4-in-row', player1, player2, board_size=(height, width))
        assert game is not None, 'Failed to initialize environment'
        game.render()  # Manual check
        assert game.available_moves(player1) != []
        assert game.available_moves(player2) != []
        assert game.player_status(player1) == 0
        assert game.player_status(player2) == 0
        assert game.is_terminal_state() is False
        assert game.apply_action(player1, 1) is not None
        assert game.apply_action(player1, 1) is None
        assert game.apply_action(player2, 1) is not None
        assert game.apply_action(player2, 1) is None
        game.render()  # Manual check
        assert game.reset is not None
        game.render()  # Manual check

    def test_horizontal_win(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 4
        height = 2
        game = create_env('4-in-row', player1, player2, board_size=(height, width))

        print(game.available_moves(player1))  # Test available moves in the beginning
        game.apply_action(player1, 0)
        game.apply_action(player2, 0)
        game.apply_action(player1, 1)
        game.apply_action(player2, 1)
        game.apply_action(player1, 2)
        game.apply_action(player2, 2)
        game.apply_action(player1, 3)

        assert game.available_moves(player1) == []
        assert game.available_moves(player2) == []
        assert game.player_status(player1) == 1
        assert game.player_status(player2) == -1
        assert game.is_terminal_state() is True
        assert game.apply_action(player2, 4) is None

    def test_vertical_win(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 2
        height = 4
        game = create_env('4-in-row', player1, player2, board_size=(height, width))
        for h in range(3):
            game.apply_action(player1, 0)
            game.apply_action(player2, 1)
        game.apply_action(player1, 0)

        assert game.available_moves(player1) == []
        assert game.available_moves(player2) == []
        assert game.player_status(player1) == 1
        assert game.player_status(player2) == -1
        assert game.is_terminal_state() is True
        assert game.apply_action(player2, 4) is None

    def test_diagonal_win(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 4
        height = 4
        game = create_env('4-in-row', player1, player2, board_size=(height, width))

        game.apply_action(player1, 0)
        game.apply_action(player2, 1)
        game.apply_action(player1, 1)
        game.apply_action(player2, 2)
        game.apply_action(player1, 1)
        game.apply_action(player2, 2)
        game.apply_action(player1, 2)
        game.apply_action(player2, 3)
        game.apply_action(player1, 3)
        game.apply_action(player2, 3)
        game.apply_action(player1, 3)

        assert game.available_moves(player1) == []
        assert game.available_moves(player2) == []
        assert game.player_status(player1) == 1
        assert game.player_status(player2) == -1
        assert game.is_terminal_state() is True
        assert game.apply_action(player2, 4) is None

    def test_reverse_diagonal_win(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 4
        height = 4
        game = create_env('4-in-row', player1, player2, board_size=(height, width))

        game.apply_action(player1, 3)
        game.apply_action(player2, 2)
        game.apply_action(player1, 2)
        game.apply_action(player2, 1)
        game.apply_action(player1, 2)
        game.apply_action(player2, 1)
        game.apply_action(player1, 1)
        game.apply_action(player2, 0)
        game.apply_action(player1, 0)
        game.apply_action(player2, 0)
        game.apply_action(player1, 0)

        assert game.available_moves(player1) == []
        assert game.available_moves(player2) == []
        assert game.player_status(player1) == 1
        assert game.player_status(player2) == -1
        assert game.is_terminal_state() is True
        assert game.apply_action(player2, 4) is None

    def test_is_terminal_state(self):
        player1 = DummyAgent('player1')
        player2 = DummyAgent('player2')
        width = 2
        height = 2
        game = create_env('4-in-row', player1, player2, board_size=(height, width))

        game.apply_action(player1, 0)
        game.apply_action(player2, 0)
        game.apply_action(player1, 1)
        game.apply_action(player2, 1)
        assert game.available_moves(player1) == []
        assert game.available_moves(player2) == []
        assert game.player_status(player1) == 0
        assert game.player_status(player2) == 0
        assert game.is_terminal_state() is True
        assert game.apply_action(player2, 4) is None

