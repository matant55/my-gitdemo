from cardpack import CardPack


def main():
    card_pack = CardPack(is_full=False)
    card_pack.shuffle()
    for card in card_pack.cards:
        print(card)


# dunder
if __name__ == "__main__":
    main()
