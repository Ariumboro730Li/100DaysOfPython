import random
import time
from art import logo
from clear_terminal import clear_terminal

def pickCard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def callResult(user, dealer):
    print(f"Your cards are : {user} : {calculateScore(user)}")
    print(f"Dealer's cards are : {dealer} : {calculateScore(dealer)}")

is_game_over = False
game_on = True
user_results = [] 
dealer_results = []

print(logo)
while game_on:
    user = [pickCard(), pickCard()]
    dealer = [11, pickCard()]
    
    def prinResult():
        return callResult(user, dealer)
        
    while not is_game_over:
        prinResult()
        if calculateScore(dealer) >= 21 or calculateScore(user) >= 21:
            is_game_over = True
            break
            
        hit_stand()
        if calculateScore(user) != 0:
            hit_stand = input("Do you want to hit / stand ? klik 'n' to stand and any button to hit \n").lower()
            if hit_stand == "n":
                is_game_over = True
            else:
                user.append(pickCard())
                if calculateScore(user) >= 21:
                    is_game_over = True
                    
            clear_terminal()
        else:
            is_game_over = True

            
    while calculateScore(dealer) < 16 and calculateScore(dealer) != 0:
        if dealer[0] == 0:
            del dealer[0]

        prinResult()
        time.sleep(1)
        dealer.append(pickCard())
        clear_terminal()
        
    prinResult()
    user_bust = False
    dealer_bust = False

    print("\n")
    
    if calculateScore(user) == 0:
        user_results.append("BLACKJACK")
        print("YOU BLACKJACK")
        if calculateScore(dealer) != 0:
            dealer_results.append("LOSE")
            print("DEALER LOSE")

    if calculateScore(dealer) == 0:
        dealer_bust = True
        dealer_results.append("BLACKJACK")
        print("DEALER BLACKJACK")
        if calculateScore(user) != 0:
            user_results.append("LOSE")
            print("USER LOSE")

    if calculateScore(user) != 0 and  calculateScore(dealer) != 0:
        if calculateScore(user) > 21:
            user_bust = True
            user_results.append("BUST")
            print("YOU BUST")

        if calculateScore(dealer) > 21:
            dealer_bust = True
            dealer_results.append("BUST")
            print("DEALER BUST")
            
        if not user_bust and not dealer_bust:
            if calculateScore(user) == calculateScore(dealer):
                user_results.append("DRAW")
                dealer_results.append("DRAW")
                print("DRAW")
            elif calculateScore(user) == 21 and calculateScore(dealer) != 21:
                user_results.append("WON")
                dealer_results.append("LOSE")
                print("YOU WON")
            elif calculateScore(user) > calculateScore(dealer) != 21:
                user_results.append("WON")
                dealer_results.append("LOSE")
                print("YOU WON")
            else: 
                user_results.append("LOSE")
                dealer_results.append("WON")
                print("YOU LOSE")


        if dealer_bust and not user_bust:
            user_results.append("WON")
            print("YOU WON")
            
        if user_bust and not dealer_bust:
            dealer_results.append("WON")
            print("DEALER WON")
        
    print("\n")
    
    print(f"Your games : {user_results}")
    print(f"dealer games : {dealer_results}")
    repeat = input("Play Again ? N for no, any button to repeat\n")
    is_game_over = False
    if repeat.lower() == "n":
        game_on = False
        
    clear_terminal()

print(f"Your games : {user_results}")
print(f"dealer games : {dealer_results}")
