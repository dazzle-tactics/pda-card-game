import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Diamonds", 10)
        self.cardGame = CardGame()
        self.cards = [self.card1, self.card2]
    
    def test_for_ace_returns_true(self):
        ace = self.cardGame.check_for_ace(self.card1)
        self.assertEqual(True, ace)
    
    def test_for_ace_returns_false(self):
        ten = self.cardGame.check_for_ace(self.card2)
        self.assertEqual(False, ten)

    def test_highest_card_returns_card2(self):
        high = self.cardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, high)

    def test_cards_total_returns_total_value(self):
        total = self.cardGame.cards_total(self.cards)
        self.assertEqual("You have a total of 11", total)