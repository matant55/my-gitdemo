class card:

    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def __str__(self):
        return f"card({self.shape},{self.number})"


class packet:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        packet_string="packet("
        for card in self.cards:
            packet_string+=str(card)+","
        return packet_string+")"
