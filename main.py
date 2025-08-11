# test_card_collection.py

from cards.card import Card
from cards.collection import CardCollection

# -------------------
# Create some sample cards
# -------------------
cards_deck = [
    Card("Ace of Hearts", "A❤️", {"color": "red", "value": 14}),
    Card("King of Hearts", "K❤️", {"color": "red", "value": 13}),
    Card("Queen of Spades", "Q♠️", {"color": "black", "value": 12}),
    Card("Ten of Hearts", "10❤️", {"color": "red", "value": 10}),
    Card("Two of Clubs", "2♣️", {"color": "black", "value": 2}),
    Card("Seven of Hearts", "7❤️", {"color": "red", "value": 7}),
]

cards_hand = [
    Card("Jack of Diamonds", "J♦️", {"color": "red", "value": 11}),
    Card("Three of Spades", "3♠️", {"color": "black", "value": 3}),
    Card("Ten of Diamonds", "10♦️", {"color": "red", "value": 10}),
    Card("Four of Spades", "4♠️", {"color": "black", "value": 4}),
]

deck = CardCollection(cards_deck)
hand = CardCollection(cards_hand)

print("\n=== Initial State ===")
print("Deck:", deck.get_cards())
print("Hand:", hand.get_cards())

# -------------------
# Example 1 — Find the second red card in the deck
# -------------------
second_red = deck.find_card(lambda c: c.attributes.get("color") == "red", nth=2)
print("\nSecond red card in deck:", second_red)

# -------------------
# Example 2 — Get all black cards in the hand
# -------------------
black_cards = hand.find_all(lambda c: c.attributes.get("color") == "black")
print("\nAll black cards in hand:", black_cards)

# -------------------
# Example 3 — Trade second red card from deck with first black card from hand
# -------------------
print("\nTrading 2nd red from deck with 1st black from hand...")
deck.trade_by_condition(
    hand,
    my_condition=lambda c: c.attributes.get("color") == "red",
    their_condition=lambda c: c.attributes.get("color") == "black",
    my_nth=2,
    their_nth=1
)

print("\n=== After Trade ===")
print("Deck:", deck.get_cards())
print("Hand:", hand.get_cards())

# -------------------
# Example 4 — Shuffle the deck
# -------------------
print("\nShuffling deck...")
deck.shuffle()
print("Deck after shuffle:", deck.get_cards())

# -------------------
# Example 5 — Trade based on value rule (any card with value <= 4)
# -------------------
print("\nTrading low-value cards (<= 4)...")
deck.trade_by_condition(
    hand,
    my_condition=lambda c: c.attributes.get("value", 0) <= 4,
    their_condition=lambda c: c.attributes.get("value", 0) <= 4
)

print("\n=== Final State ===")
print("Deck:", deck.get_cards())
print("Hand:", hand.get_cards())
