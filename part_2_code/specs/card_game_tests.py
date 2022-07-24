import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 10)
        self.card3 = Card("Clubs", 1)
        self.card4 = Card("Diamonds", 11)
        self.cards = [self.card1, self.card2]

        self.game1 = CardGame()

    def test_card_is_ace(self):
        result = CardGame.check_for_ace(self.game1, self.card1)
        self.assertEqual(True, result)

    def test_card1_is_higher(self):
        results = CardGame.highest_card(self.game1, self.card2, self.card1)
        self.assertEqual(self.card2, results)

    def test_card2_is_higher(self):
        results = CardGame.highest_card(self.game1, self.card1, self.card4)
        self.assertEqual(self.card4, results)

    def test_cards_can_be_equal(self):
        results = CardGame.highest_card(self.game1, self.card1, self.card3)
        self.assertEqual("Cards are of equal value", results)

    def test_return_card_total(self):
        results = CardGame.cards_total(self.game1, self.cards)
        self.assertEqual("You have a total of 11", results)