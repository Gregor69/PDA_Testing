import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("suit", 1)
        self.card_game = CardGame
        self.card1 = Card("suit", 3)
        self.card2 = Card("suit", 2)
        self.cards = CardGame("cards")
        self.cards.total = CardGame("cards total")

        
        
     


    def test_check_for_ace(self):
        self.card.value == 1
        self.assertEqual(1, self.card.value)

    def test_get_highest_card(self):
        self.card1.value > self.card2.value
        self.assertGreater(self.card1.value)

    def test_get_cards_total(self):
        self.cards.total
        self.assertEqual(self.cards.total)

  


