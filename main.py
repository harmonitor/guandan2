from card import *

a = Deck(master_num = 3)
print(a.face_to_values)

a.shuffle()
for card in a.cards:
    print(card.get_value(),card.get_suit())

# print(a.cards[51].get_suit())