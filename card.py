"""defines properties and behavior of a single playing card"""


class Card:

    def __init__(self, rank, suit):
        self.__dictionary = {'rank': rank, 'suit': suit}
        self.__rank = self.__dictionary['rank']
        self.__suit = self.__dictionary['suit']

    def get_rank(self):
        """return the rank of this card"""
        return self.__rank

    def get_suit(self):
        """return the suit of this card"""
        return self.__suit

    def __str__(self):
        """return this card as a printable string"""
        rank = self.get_rank()
        suit = self.get_suit()

        if suit == "H":
            suit_string = "Hearts"
        elif suit == "D":
            suit_string = "Diamonds"
        elif suit == "S":
            suit_string = "Spades"
        elif suit == "C":
            suit_string = "Clubs"
        else:
            suit_string = suit

        if rank == 14:
            rank_string = "Ace"
        elif rank == 10:
            rank_string = "Ten"
        elif rank == 11:
            rank_string = "Jack"
        elif rank == 12:
            rank_string = "Queen"
        elif rank == 13:
            rank_string = "King"
        else:
            rank_string = rank

        return str(rank_string) + " of " + suit_string
