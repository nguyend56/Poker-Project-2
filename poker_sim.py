
from poker_hand import *
from deck import *


def deal_a_hand(deck_of_card):
    """
    this function return a hand dealt from a deck of card
    :param deck_of_card: a deck of card which is a list containing 52 card objects
    :return: a hand containing 5 card object
    """
    card_list = []
    hand = PokerHand(card_list)
    for i in range(5):
        hand.add_card(deck_of_card.deal())
    return hand


def count_vowels(s):
    """
    returns the number of vowels (a,e,i,o,u) in the string s
    """
    if len(s) == 0:
        return 0
    elif s[0] in ['a', 'e', 'i', 'o', 'u']:
        return 1 + count_vowels(s[1:len(s)])
    else:
        return count_vowels(s[1:len(s)])


def __private_count_vowels(s, starting_index):
    """
    returns number of vowels in the substring of s that
    starts at index starting_index
    """
    vowel_list = ["a", "e", "i", "o", "u"]
    if starting_index == len(s):
        return 0
    elif s[starting_index] in vowel_list:
        return 1 + __private_count_vowels(s, starting_index + 1)
    else:
        return __private_count_vowels(s, starting_index + 1)


def main():
    """
    simulate a comparing two poker hands game, ask the user which hand is a better one. Count points and end the game
    when the player guess is incorrect or the deck runs out of cards to deal two hands.
    """
    deck = Deck()
    deck.shuffle()
    game_condition = True
    player_points = 0
    while game_condition and deck.size() >= 10:
        first_hand = deal_a_hand(deck)
        second_hand = deal_a_hand(deck)
        print("The first hand is:", "\n", first_hand)
        print("The second hand is:", "\n", second_hand)
        user_guess = int(input("Who is the winner? \nYour answer: "))
        if user_guess == first_hand.compare_to(second_hand):
            player_points += 1
            print("Your point is:", player_points)
            print()
        else:
            print("Game over, your point is", player_points)
            game_condition = False


if __name__ == '__main__':
    main()
