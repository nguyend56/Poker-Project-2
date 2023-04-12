"""test compare_to function in poker_hand module by running some test case"""

from poker_hand import *
from card import *
from testing import *


def test_compare_to():
    """ all compare_to tests"""
    start_tests("compare_to function testing")
    test_flush_hand_and_two_pair_hand()
    test_two_pair_hand_and_pair_hand()
    test_pair_hand_and_high_card_hand()
    test_high_card_hand_and_flush_hand()
    test_two_pair_hand_and_flush_hand()
    test_two_pair_hand_and_high_card_hand()
    test_flush_hands()
    test_two_pair_hands_that_have_different_pairs()
    test_two_pair_hands_that_have_same_one_pair()
    test_two_pair_hands_that_have_same_two_pairs()
    test_pair_hands_that_have_different_pair()
    test_pair_hands_that_have_same_pair()
    test_pair_hands_that_have_same_pair_and_same_highest_high_card()
    test_pair_hands_that_have_same_pair_and_same_highest_and_second_highest_high_card()
    test_two_different_high_card_hands()
    test_two_high_card_hands_that_have_same_highest_high_card()
    test_two_high_card_hands_that_have_same_highest__and_second_highest_high_card()
    test_two_high_card_hands_that_have_same_three_highest_high_card()
    test_two_high_card_hands_that_have_only_one_different_card()
    two_equal_hand()
    finish_tests()


""" Unit tests start below """

"""Test hands with different types"""


def test_flush_hand_and_two_pair_hand():
    cards_in_flush_hand = [Card(4, "S"), Card(5, "S"), Card(6, "S"), Card(7, "S"), Card(8, "S")]
    flush_hand = PokerHand(cards_in_flush_hand)
    cards_in_two_pair_hand = [Card(4, "S"), Card(4, "C"), Card(6, "S"), Card(6, "D"), Card(8, "S")]
    two_pair_hand = PokerHand(cards_in_two_pair_hand)
    actual = flush_hand.compare_to(two_pair_hand)
    expect = 1
    assert_equals("comparing a flush hand to a two-pair hand", expect, actual)


def test_two_pair_hand_and_pair_hand():
    cards_in_two_pair_hand = [Card(14, "D"), Card(5, "S"), Card(14, "H"), Card(7, "S"), Card(7, "D")]
    two_pair_hand = PokerHand(cards_in_two_pair_hand)
    cards_in_pair_hand = [Card(4, "S"), Card(4, "C"), Card(6, "S"), Card(10, "D"), Card(8, "S")]
    pair_hand = PokerHand(cards_in_pair_hand)
    actual = two_pair_hand.compare_to(pair_hand)
    expect = 1
    assert_equals("comparing a two-pair hand to a pair hand", expect, actual)


def test_pair_hand_and_high_card_hand():
    cards_in_pair_hand = [Card(14, "D"), Card(5, "S"), Card(11, "H"), Card(7, "S"), Card(7, "D")]
    pair_hand = PokerHand(cards_in_pair_hand)
    cards_in_high_card_hand = [Card(4, "S"), Card(7, "C"), Card(6, "S"), Card(10, "D"), Card(8, "S")]
    high_card_hand = PokerHand(cards_in_high_card_hand)
    actual = pair_hand.compare_to(high_card_hand)
    expect = 1
    assert_equals("comparing a pair hand to a high card hand", expect, actual)


def test_high_card_hand_and_flush_hand():
    cards_in_high_card = [Card(5, "H"), Card(9, "D"), Card(2, "S"), Card(8, "C"), Card(12, "S")]
    high_card_hand = PokerHand(cards_in_high_card)
    cards_in_flush_hand = [Card(10, "S"), Card(9, "S"), Card(11, "S"), Card(8, "S"), Card(12, "S")]
    flush_hand = PokerHand(cards_in_flush_hand)
    actual = high_card_hand.compare_to(flush_hand)
    expect = -1
    assert_equals("comparing a high card hand to a flush hand", expect, actual)


def test_two_pair_hand_and_flush_hand():
    cards_in_two_pair_hand = [Card(14, "D"), Card(5, "S"), Card(14, "H"), Card(7, "S"), Card(7, "D")]
    two_pair_hand = PokerHand(cards_in_two_pair_hand)
    cards_in_flush_hand = [Card(6, "C"), Card(7, "C"), Card(9, "C"), Card(10, "C"), Card(8, "C")]
    flush_hand = PokerHand(cards_in_flush_hand)
    actual = two_pair_hand.compare_to(flush_hand)
    expect = -1
    assert_equals("comparing a two-pair hand to a flush hand", expect, actual)


def test_two_pair_hand_and_high_card_hand():
    cards_in_two_pair_hand = [Card(14, "D"), Card(5, "S"), Card(14, "H"), Card(7, "S"), Card(7, "D")]
    two_pair_hand = PokerHand(cards_in_two_pair_hand)
    cards_in_high_card_hand = [Card(6, "S"), Card(7, "C"), Card(2, "D"), Card(10, "H"), Card(4, "C")]
    high_card_hand = PokerHand(cards_in_high_card_hand)
    actual = two_pair_hand.compare_to(high_card_hand)
    expect = 1
    assert_equals("comparing a two-pair hand to a high card hand", expect, actual)


"""Test hands with same type"""


def test_flush_hands():
    cards_in_first_hand = [Card(5, "H"), Card(6, "H"), Card(4, "H"), Card(13, "H"), Card(6, "H")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(13, "C"), Card(10, "C"), Card(11, "C"), Card(14, "C"), Card(12, "C")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two flush hands", expect, actual)


def test_two_pair_hands_that_have_different_pairs():
    cards_in_first_hand = [Card(5, "H"), Card(5, "S"), Card(12, "C"), Card(7, "H"), Card(7, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(2, "C"), Card(6, "D"), Card(6, "C"), Card(8, "C"), Card(8, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two two-pair hands that have different pairs", expect, actual)


def test_two_pair_hands_that_have_same_one_pair():
    cards_in_first_hand = [Card(5, "H"), Card(5, "S"), Card(12, "C"), Card(7, "H"), Card(7, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(7, "C"), Card(2, "D"), Card(2, "C"), Card(7, "D"), Card(2, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two two-pair hands that have the same one pair", expect, actual)


def test_two_pair_hands_that_have_same_two_pairs():
    cards_in_first_hand = [Card(5, "H"), Card(5, "S"), Card(12, "C"), Card(7, "H"), Card(7, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(7, "C"), Card(5, "D"), Card(5, "C"), Card(7, "D"), Card(2, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two two-pair hands that have the same two pairs", expect, actual)


def test_pair_hands_that_have_different_pair():
    cards_in_first_hand = [Card(8, "H"), Card(3, "S"), Card(11, "C"), Card(11, "H"), Card(2, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(9, "C"), Card(5, "D"), Card(5, "C"), Card(4, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two pair hands that have different pair", expect, actual)


def test_pair_hands_that_have_same_pair():
    cards_in_first_hand = [Card(8, "H"), Card(3, "S"), Card(14, "C"), Card(14, "H"), Card(2, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(9, "C"), Card(14, "D"), Card(14, "C"), Card(4, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two pair hands that have same pair", expect, actual)


def test_pair_hands_that_have_same_pair_and_same_highest_high_card():
    cards_in_first_hand = [Card(8, "H"), Card(3, "S"), Card(10, "C"), Card(10, "H"), Card(14, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "C"), Card(14, "D"), Card(4, "C"), Card(10, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two pair hands that have same pair and same highest high card", expect, actual)


def test_pair_hands_that_have_same_pair_and_same_highest_and_second_highest_high_card():
    cards_in_first_hand = [Card(6, "H"), Card(3, "S"), Card(10, "C"), Card(10, "H"), Card(14, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "C"), Card(14, "D"), Card(4, "C"), Card(10, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two pair hands that have same pair "
                  "and same highest and second highest high card", expect, actual)


def test_two_different_high_card_hands():
    cards_in_first_hand = [Card(8, "H"), Card(3, "S"), Card(10, "C"), Card(5, "H"), Card(4, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "C"), Card(12, "D"), Card(4, "C"), Card(9, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two different high card hands", expect, actual)


def test_two_high_card_hands_that_have_same_highest_high_card():
    cards_in_first_hand = [Card(8, "H"), Card(3, "S"), Card(10, "C"), Card(5, "H"), Card(4, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "C"), Card(5, "D"), Card(4, "C"), Card(9, "D"), Card(6, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two high card hands that have same highest high card", expect, actual)


def test_two_high_card_hands_that_have_same_highest__and_second_highest_high_card():
    cards_in_first_hand = [Card(8, "H"), Card(11, "S"), Card(10, "C"), Card(5, "H"), Card(4, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "D"), Card(5, "D"), Card(4, "C"), Card(2, "D"), Card(11, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two high card hands that have same highest and second highest high card", expect, actual)


def test_two_high_card_hands_that_have_same_three_highest_high_card():
    cards_in_first_hand = [Card(8, "H"), Card(11, "S"), Card(10, "C"), Card(5, "H"), Card(12, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "D"), Card(5, "D"), Card(4, "C"), Card(12, "D"), Card(11, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 1
    assert_equals("comparing two high card hands that have same highest and second highest high card", expect, actual)


def test_two_high_card_hands_that_have_only_one_different_card():
    cards_in_first_hand = [Card(5, "H"), Card(11, "S"), Card(10, "C"), Card(2, "H"), Card(12, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "D"), Card(5, "D"), Card(4, "C"), Card(12, "D"), Card(11, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = -1
    assert_equals("comparing two high card hands that have only one different card", expect, actual)


def two_equal_hand():
    cards_in_first_hand = [Card(5, "H"), Card(11, "S"), Card(10, "C"), Card(7, "H"), Card(12, "C")]
    first_hand = PokerHand(cards_in_first_hand)
    cards_in_second_hand = [Card(10, "D"), Card(5, "D"), Card(7, "C"), Card(12, "D"), Card(11, "S")]
    second_hand = PokerHand(cards_in_second_hand)
    actual = first_hand.compare_to(second_hand)
    expect = 0
    assert_equals("comparing two equal hands", expect, actual)


if __name__ == "__main__":
    test_compare_to()
