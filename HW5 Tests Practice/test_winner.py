import unittest
from game import TicTacToe


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_winner_row(self):
        self.game.board = ['O', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'O']
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertFalse(self.game.winner(2, 'X'))
        self.assertFalse(self.game.winner(3, 'O'))

    def test_winner_column(self):
        self.game.board = ['X', ' ', 'O', 'X', 'O', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(4, 'X'))

    def test_winner_diagonal1(self):
        self.game.board = ['O', 'X', 'X', ' ', 'O', 'X', ' ', ' ', 'O']
        self.assertTrue(self.game.winner(4, 'O'))
        self.assertTrue(self.game.winner(0, 'O'))
        self.assertFalse(self.game.winner(8, 'X'))

    def test_winner_diagonal2(self):
        self.game.board = ['O', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'O']
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(4, 'O'))


if __name__ == '__main__':
    unittest.main()
