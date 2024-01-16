from card import card, packet


class cardsexecuter:
    def create_full_packet(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards=[]
        for suit in suits:
            for rank in ranks:
                cards.append(card(rank,suit))
        pkt = packet(cards)
        print(pkt)
    def create_partof_packet(self):
        ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards = []
        for suit in suits:
            for rank in ranks:
                cards.append(card(rank, suit))
        pkt = packet(cards)
        print(pkt)

c= cardsexecuter()
c.create_full_packet()
c.create_partof_packet()
