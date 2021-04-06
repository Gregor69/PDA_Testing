import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts", 1)
        self.card_game = CardGame()
        self.card1 = Card("spades", 3)
        self.card2 = Card("clubs", 2)
        
    def test_check_for_ace(self):
        result = self.card_game.check_for_ace(self.card)
        self.assertEqual(True, result)

    
    def test_get_highest_card(self):
        self.assertEqual(self.card1, self.card_game.get_highest_card(self.card1, self.card2))

    def test_get_cards_total(self):
        self.card1 = Card("spades", 3)
        self.card2 = Card("clubs", 2)
        cards_list = [self.card1, self.card2]
        self.assertEqual("You have a total of 5", CardGame().get_cards_total(cards_list))





