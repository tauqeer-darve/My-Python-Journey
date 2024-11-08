import random
import blackjack_art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(score_comp,score_user):
    if score_comp == score_user:
        print("Draw")
    elif score_comp == 0:
        print("Opponent has a Blackjack, You Lose.")
    elif score_user == 0:
        print("You have a Blackjack, You Win!")
    elif score_user > 21:
        print("You went over, You Lose.")
    elif score_comp > 21:
        print("Opponent went over, You win!")
    elif score_user > score_comp:
        print("You Win.")
    else:
        print("You Lose.")

def blackjack():
    print(blackjack_art.logo)
    user = []
    comp = []
    comp_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())

    while not game_over:
        user_score = calculate_score(user)
        comp_score = calculate_score(comp)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Opponent's first card: {comp[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                user.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp.append(deal_card())
        comp_score = calculate_score(comp)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Opponent's final hand: {comp}, final score: {comp_score}")
    compare(comp_score,user_score)

print("\n")
while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 50)
    blackjack()



