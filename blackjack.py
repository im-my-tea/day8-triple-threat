import random
import art

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for Blackjack (Ace + 10) AND only 2 cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 represents Blackjack in our game
        
    # Check for Ace (11) if score > 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == 0:
        return "Blackjack! You win!"
    elif dealer_score == 0:
        return "Blackjack! Dealer wins!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif user_score == dealer_score:
        return "Draw!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"


def main():
    print(art.blackjack_logo)
    user_cards = []
    dealer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
            continue
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                continue
            else:
                is_game_over = True
                break
        
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
     
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))
    again = int(input("Do you want to play again? (yes - 1/no - *): "))
    if again == 1:
        main()
    else:
        print("Goodbye!")

        
main()
