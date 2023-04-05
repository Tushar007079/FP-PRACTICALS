from random import randint
def pick_card():
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    card = randint(0, 51)
    card_val = card % 13
    card_suit = int(card/13)
    return [suits[card_suit], values[card_val]]

picks = 0
suits_picked = []
number_picked = []
while len(suits_picked) != 4:
    card = pick_card()
    if card[0] not in suits_picked:
        suits_picked.append(card[0])
        number_picked.append(card[1])
        picks += 1
print(f'Number of picks: {picks}')
for i in range(0, 4):
    print(number_picked[i], ' of ', suits_picked[i])
print('\n')
