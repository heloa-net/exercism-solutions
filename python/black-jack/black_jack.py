"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """
    Get the value of the card

    :param card: str - card to find out the value for
    """

    ace = 'A'
    face_cards = ['J', 'Q', 'K']

    if card in face_cards:
        return 10
    if card == ace:
        return 1

    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value_one, value_two = value_of_card(card_one), value_of_card(card_two)

    if value_one == value_two:
        return card_one, card_two
    if value_one > value_two:
        return card_one

    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    hand = [card_one, card_two]
    ace = 'A'
    hand_value = value_of_card(card_one) + value_of_card(card_two) # try with currying

    if ace in hand or hand_value > 10:
        return 1

    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ace = 'A'
    value_ten = ['J', 'Q', 'K', '10']

    hand = [card_one, card_two]

    if ace in hand and (card_one in value_ten or card_two in value_ten):
        return True

    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    face_cards = ['J', 'Q', 'K']

    twin_hand = card_one == card_two
    face_cards_only = card_one in face_cards and card_two in face_cards

    return twin_hand or face_cards_only

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    value_one, value_two = value_of_card(card_one), value_of_card(card_two)
    hand_value = value_one + value_two

    return 9 <= hand_value <= 11
