#!/usr/bin/env python3
try:
    from ..envs import *
    from ..agents import *
except (ImportError, ValueError):
    import os
    import sys
    parentdir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    sys.path.insert(0, parentdir)
    from envs import *
    from agents import *

import mock
import pytest


class DummyAgent(Agent):
    def choose_action(self, env):
        pass


class TestAgents(object):
    @mock.patch('agents.HumanAgent.choose_action')
    def test_human_agent(self, monkeypatch):
        human = HumanAgent('human')
        dummy = DummyAgent('dummy')
        width = 4
        height = 2

        game = create_env('4-in-row', human, dummy, board_size=(height, width))
        assert game is not None, 'Failed to initialize environment'
        game.render()  # Manual check
        assert game.available_moves(human) != []
        assert game.available_moves(dummy) != []
        assert game.player_status(human) == 0
        assert game.player_status(dummy) == 0
        assert game.is_terminal_state() is False
        mock.side_effect = ['1', '2', '3', '4']
        for m in range(1, 5):
            assert game.apply_action(human, human.choose_action(game)) is not None
            assert game.apply_action(dummy, m) is None

    def test_alphabeta_agents(self):
        pass
