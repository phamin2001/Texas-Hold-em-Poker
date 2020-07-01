import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator


class StraightFlushValidatorTest(unittest.TestCase):
    # def setUp(self):
    #     self.three_of_clubs = Card(rank="3", suit="Clubs")
    #     self.four_of_clubs = Card(rank="4", suit="Clubs")
    #     self.five_of_clubs = Card(rank="5", suit="Clubs")
    #     self.six_of_clubs = Card(rank="6", suit="Clubs")
    #     self.seven_of_clubs = Card(rank="7", suit="Clubs")

    #     self.cards = [
    #         self.three_of_clubs,
    #         self.four_of_clubs,
    #         self.five_of_clubs,
    #         self.six_of_clubs,
    #         self.seven_of_clubs
    #     ]

    def test_determines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
            Card(rank="6", suit="Clubs"),
            Card(rank="7", suit="Diamonds"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds")
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
            Card(rank="6", suit="Clubs"),
            Card(rank="7", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds")
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
