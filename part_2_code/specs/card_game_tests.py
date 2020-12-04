import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def test_check_ace(self):
        self.card_game = CardGame()
        self.card = Card("club", 1)
        self.assertEqual(True, self.card_game.check_for_ace(self.card))

    def test_highest_card(self):
        self.card_game = CardGame()
        self.card1 = Card("heart", 5)
        self.card2 = Card("spade", 7)
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_card_total(self):
        self.card_game = CardGame()
        self.card1 = Card("heart", 5)
        self.card2 = Card("spade", 7)
        self.cards = [self.card1, self.card2]
        results = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 12", results)