from card import Card, packet
from typing import List
import random


class CardPack:
    FULL_RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "JK")
    PART_OF_RANKS = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __init__(self, is_full: bool = True):
        self.cards = self.create_packet(is_full)

    def create_packet(self, is_full: bool = True) -> List[Card]:
        """Create a list of cards based on is_ful"""
        cards = []
        if is_full:
            ranks = self.FULL_RANKS
        else:
            ranks = self.PART_OF_RANKS
        # ranks = self.FULL_RANKS if is_full else self.PART_OF_RANKS
# Instance
        for suit in self.SUITS:
            for rank in ranks:
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)
