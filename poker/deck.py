import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_cards(self, number):
        cards_to_removes = self.cards[:number]
        del self.cards[:number]
        return cards_to_removes

    def shuffle(self):
        random.shuffle(self.cards)

