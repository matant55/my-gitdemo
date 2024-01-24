class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} {self.suit}"


class packet:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        packet_string = "packet("
        for card in self.cards:
            packet_string += str(card) + ","
        return packet_string + ")"
