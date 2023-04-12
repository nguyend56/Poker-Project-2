"""defines a standard deck of 52 playing cards"""

import random
from card import *

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
SUITS = ["H", "D", "S", "C"]


class Deck:
    def __init__(self):
        self.__contents = []
        for rank in RANKS:
            for suit in SUITS:
                new_card = Card(rank, suit)
                self.__contents.append(new_card)

    def shuffle(self):
        """
        this function shuffles the cards in the deck
        :return: a shuffled deck of card
        """
        random.shuffle(self.__contents)
        return self.__contents

    def deal(self):
        """
        return the card at the top of the deck
        :return: card object or null if deck empty
        """
        if len(self.__contents) == 0:
            return None
        else:
            return self.__contents.pop(0)

    def size(self):
        """
        this function return number of cards left in the deck after dealing cards
        :return: an integer demonstrating number of cards left in deck
        """
        return len(self.__contents)

    def __str__(self):
        """
        return a printable version of the deck, one card at a time
        :return: strong that shows all cards currently in the deck
        """
        printable_deck = ""
        for card in self.__contents:
            printable_deck += str(card) + "\n"
        return printable_deck
