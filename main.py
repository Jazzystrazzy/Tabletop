from cards.decks import Deck, FrenchDeck

# -------------------
# Create some sample cards
# -------------------

full_deck = FrenchDeck()

stack = Deck(full_deck.draw_n_cards(n=10, from_where="random"))
hand = Deck(full_deck.draw_n_cards(n=5, from_where="random"))

print("\n=== Initial State ===")
print("Deck:", stack.to_list())
print("Hand:", hand.to_list())

# -------------------
# Example 1 — Find the second red card in the deck
# -------------------
second_red = stack.find_card(lambda c: c.attributes.get("color") == "red", nth=2)
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
stack.trade_by_condition(
    hand,
    my_condition=lambda c: c.attributes.get("color") == "red",
    their_condition=lambda c: c.attributes.get("color") == "black",
    my_nth=2,
    their_nth=1
)

print("\n=== After Trade ===")
print("Deck:", stack.to_list())
print("Hand:", hand.to_list())

# -------------------
# Example 4 — Shuffle the deck
# -------------------
print("\nShuffling stack...")
stack.shuffle()
print("Deck after shuffle:", stack.to_list())

# -------------------
# Example 5 — Trade based on value rule (all cards with value <= 4)
# -------------------
print("\nTrading low-value cards (<= 4)...")
stack.trade_all_by_condition(
    hand,
    my_condition=lambda c: c.attributes.get("value", 0) <= 4,
    their_condition=lambda c: c.attributes.get("value", 0) <= 4,
)

print("\n=== Final State ===")
print("Deck:", stack.to_list())
print("Hand:", hand.to_list())
