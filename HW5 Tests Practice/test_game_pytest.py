import pytest
from game import TicTacToe


game = TicTacToe()
game.board[4] = "X"


def test_available_moves():
    assert 4 not in game.available_moves()


def test_make_move():
    assert not game.make_move(4, "X")
    assert game.make_move(5, "X")
    assert game.board[5] != " "
