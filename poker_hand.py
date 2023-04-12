"""defines properties and behavior of a single playing hand which consists 5 card. Compare two hands to see which
one is a better hand."""


class PokerHand:

    def __init__(self, list_of_card):
        self.__hand = list_of_card[:]

    def add_card(self, card):
        """return the card which is added to player's hand"""
        return self.__hand.append(card)

    def get_ith_card(self, index):
        """return the the card at the assigned index"""
        return self.__hand[index]

    def __str__(self):
        """
        return a printable version of the hand, one card per time
        :return: string that shows all cards currently in the hand
        """
        printable_hand = ""
        for card in self.__hand:
            printable_hand += str(card) + "\n"
        return printable_hand

    def check_type(self):
        """
        determine which category the hand is
        :return: 3 if it's a flush, 2 if it's a two-pair, 1 if it's a pair and 0 if it's a high-card
        """
        root = self.__hand[0].get_suit()
        count = 0
        for card in self.__hand:
            if card.get_suit() == root:
                count += 1
        if count == 5:
            return 3  # Flush
        else:
            pair_count = 0
            for i in range(len(self.__hand)):
                for j in range(i):              # this nested loop checks how many single pairs in player's hand.
                    if self.__hand[i].get_rank() == self.__hand[j].get_rank():
                        pair_count += 1
            if pair_count == 2 or pair_count == 4 or pair_count == 6:
                # in 2 pairs category, there will be 2 separated pairs, thus if number of pair_count equals 2, this hand
                # is a two pair. Similarly, full house category has 4 single pairs (3 single pairs from 3 cards with the
                # same rank and 1 single pair from the 2 other cards left), four of a kind category has 6 single pairs
                # from 4 cards with the same rank.
                return 2  # 2 pairs
            if pair_count == 1 or pair_count == 3:
                # in pair category, there will be 1 single pair, thus if number of pair_count equals 1, this hand is a
                # pair in three of a kind category, 3 cards of a same rank have 3 single pairs, thus if number of
                # pair_count equals 3, this hand is a three of a kind.
                return 1  # pair
            else:
                return 0  # high card

    def full_house_outlier(self):
        """
        determine the higher-rank pair in a full house hand
        :return: a card in higher-rank pair if the hand is a full house, otherwise return a string "nothing"
        """
        self_ranks = []
        for card in self.__hand:
            self_ranks.append(card.get_rank())
        self_ranks.sort()
        if self_ranks[0] == self_ranks[1] and self_ranks[2] == self_ranks[3] == self_ranks[4]:
            return self_ranks[2]
        elif self_ranks[3] == self_ranks[4] and self_ranks[0] == self_ranks[1] == self_ranks[2]:
            return self_ranks[0]
        else:
            return "nothing"

    def two_pair_and_4_of_a_kind_outlier(self):
        """
        determine the card which is not in a pair of a two-pair or four of a kind hand
        :return: a card which is not in a pair of a two-pair or four of a kind hand, otherwise return a string "nothing"
        """
        self_ranks = []
        for card in self.__hand:
            self_ranks.append(card.get_rank())
        self_ranks.sort()
        if self_ranks[1] == self_ranks[2] and self_ranks[3] == self_ranks[4]:
            return self_ranks[0]
        elif self_ranks[0] == self_ranks[1] and self_ranks[3] == self_ranks[4]:
            return self_ranks[2]
        elif self_ranks[0] == self_ranks[1] and self_ranks[2] == self_ranks[3]:
            return self_ranks[4]
        else:
            return "nothing"

    def find_pair(self):
        """
        determine the pair in a pair hand
        :return: a card of the pair in the hand
        """
        self_ranks = []
        for card in self.__hand:
            self_ranks.append(card.get_rank())
        self_ranks.sort()
        if self_ranks[0] == self_ranks[1]:
            return self_ranks[0]
        elif self_ranks[1] == self_ranks[2]:
            return self_ranks[1]
        elif self_ranks[2] == self_ranks[3]:
            return self_ranks[2]
        elif self_ranks[3] == self_ranks[4]:
            return self_ranks[3]

    def compare_to(self, other_hand):
        """
        determine which hand is the better hand: self or other_hand
        :param other_hand: a list containing 5 card objects
        :return: integer 1 if self is the better hand, -1 if other_hand is the better one, 0 if they tie
        """
        if self.check_type() > other_hand.check_type():
            return 1
        elif self.check_type() < other_hand.check_type():
            return -1
        else:  # when two hands have the same type
            self_ranks = []
            other_hand_ranks = []
            last_card_index = 4
            number_of_card_in_one_hand = 5
            for card in self.__hand:
                self_ranks.append(card.get_rank())
            for i in range(number_of_card_in_one_hand):
                other_hand_ranks.append(other_hand.get_ith_card(i).get_rank())
            self_ranks.sort()
            other_hand_ranks.sort()

            """two hands are flushes"""
            if self.check_type() == other_hand.check_type() == 3:
                for i in range(number_of_card_in_one_hand):
                    if self_ranks[last_card_index - i] > other_hand_ranks[last_card_index - i]:
                        return 1
                    if self_ranks[last_card_index - i] < other_hand_ranks[last_card_index - i]:
                        return -1
                else:
                    return 0

            """two hands are two-pair"""
            if self.check_type() == other_hand.check_type() == 2:

                if self.full_house_outlier() != "nothing":
                    self_outlier = self.full_house_outlier()
                    self_ranks.remove(self_outlier)
                elif self.two_pair_and_4_of_a_kind_outlier() != "nothing":
                    self_outlier = self.two_pair_and_4_of_a_kind_outlier()
                    self_ranks.remove(self_outlier)
                else:
                    self_outlier = 0

                if other_hand.full_house_outlier() != "nothing":
                    other_hand_outlier = other_hand.full_house_outlier()
                    other_hand_ranks.remove(other_hand_outlier)
                elif other_hand.two_pair_and_4_of_a_kind_outlier() != "nothing":
                    other_hand_outlier = other_hand.two_pair_and_4_of_a_kind_outlier()
                    other_hand_ranks.remove(other_hand_outlier)
                else:
                    other_hand_outlier = 0

                if self_ranks[last_card_index - 1] > other_hand_ranks[last_card_index - 1]:  # comparing the second pair
                    #  self_ranks and other_hand_ranks have removed their outlier,
                    #  thus there are only 4 cards left in each
                    return 1
                if self_ranks[last_card_index - 1] < other_hand_ranks[last_card_index - 1]:
                    return -1
                else:
                    if self_ranks[0] > other_hand_ranks[0]:  # comparing the first pair
                        return 1
                    if self_ranks[0] < other_hand_ranks[0]:
                        return -1
                    else:
                        if self_outlier > other_hand_outlier:  # comparing the outliers
                            return 1
                        if self_outlier < other_hand_outlier:
                            return -1
                        else:
                            return 0

            """two hands are pair"""
            if self.check_type() == other_hand.check_type() == 1:

                self_pair = self.find_pair()
                self_ranks.remove(self_pair)
                other_pair = other_hand.find_pair()
                other_hand_ranks.remove(other_pair)

                number_of_card_left = 3
                if self_pair > other_pair:
                    return 1
                if self_pair < other_pair:
                    return -1
                else:
                    for i in range(1, number_of_card_left + 1):
                        if self_ranks[number_of_card_left - i] > other_hand_ranks[number_of_card_left - i]:
                            return 1
                        if self_ranks[number_of_card_left - i] < other_hand_ranks[number_of_card_left - i]:
                            return -1
                    else:
                        return 0

            """two hands are high card"""
            if self.check_type() == other_hand.check_type() == 0:  # if two hands are high cards
                for i in range(number_of_card_in_one_hand):
                    if self_ranks[last_card_index - i] > other_hand_ranks[last_card_index - i]:
                        return 1
                    if self_ranks[last_card_index - i] < other_hand_ranks[last_card_index - i]:
                        return -1
                else:
                    return 0
