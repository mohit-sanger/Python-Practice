import random

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

print(deal_card())

def calculate_score(cards):
    """It return the score of cards"""
    if sum(user_card) == 21 and len(user_card) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_card = []
computer_card = []
is_game_over = False
print(user_card)

for i in range(2):
    new_card = deal_card
    user_card.append(new_card)
    computer_card.append(new_card)

user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)

print(f" Your card: {user_card} and your score{user_score}")
print(f"computer card {computer_card[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True



