import unittest
from bowling_game import  BowlingGame

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game(self):
        for x in range(1, 21):
            self.game.roll(0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        for x in range(1, 21):
            self.game.roll(1)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self.game.roll(9)
        self.game.roll(1)
        self.game.roll(5)
        for x in range(4, 21):
            self.game.roll(0)
        self.assertEqual(20, self.game.score())

    