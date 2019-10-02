#this is a simple one player blackjack simulation
#following the concept that each card is randomly
#chosen from a mix of multiple decks

#going to follow the rules provided by 
#https://bicyclecards.com/how-to-play/blackjack/
#only difference is not including splitting pairs for now

import random

print("Welcome to Blackjack at Daniel's Casino!")
print("If you aren't familiar with blackjack, you can follow this link:")
print("https://bicyclecards.com/how-to-play/blackjack/")
balance = 100
print("We'll start with $" + str(balance) + " and you can bet either $5, $10, $25, or $100 each round")
starting_values = [5, 10, 25, 100]

#dict of cards with their value
cards = {
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 1
}
for i in range(2, 11):
    cards[str(i)] = i

#returns a randomly selected card
def card():
    return random.choice(list(cards.keys()))

#determines value of hand assuming aces are worth 1
def hand_value(hand):
    val = 0
    for card in hand:
        val += cards[card]
    if val == 11 and "A" in hand:
        return 21
    return val

#finds the maximum hand value
def max_hand_value(hand):
    val = hand_value(hand)
    if "A" in hand:
        val += 10
    return val

#blackjack check
def blackjack(value):
    return value == 21

#checks if player or dealer has gone over/busted
def over(value):
    return value > 21

#game loop while there is a balance
while balance:
    print()
    print("Your current balance is: " + str(balance))
    print("Here are the values you can bet: ")
    accepted_values = list(filter(lambda x: x <= balance, starting_values))
    print(accepted_values)
    #input loop
    while True:
        try:
            bet_value = int(input("Please choose your bet: "))
            if bet_value not in accepted_values:
                raise ValueError
        except ValueError:
            print("Sorry, please choose a presented value!")
            continue
        else:
            break

    print()
    balance -= bet_value
    dealer = [card(), card()]
    player = [card(), card()]
    dealer_val = hand_value(dealer)
    player_val = hand_value(player)
    print("Your cards are: ")
    print(player)
    print("The dealer's top card is: " + dealer[-1])

    #case of dealer blackjack
    if blackjack(dealer_val) and dealer[-1] == "A":
        if blackjack(player_val):
            print("Blackjack all around, new deal!")
            balance += bet_value
            continue
        else:
            print("Dealer won, better luck next time!")
            continue

    #case of player blackjack
    if blackjack(player_val):
        if blackjack(dealer_val):
            print("Blackjack all around, new deal!")
            balance += bet_value
            continue
        else:
            print("You got Blackjack! You win!")
            balance += int(1.5 * bet_value)
            continue
    
    #this is the sequence where the player can choose to hit for more cards
    while not over(player_val):
        while True:
            try:
                hit = input("Do you want to hit for one more card? (y/n) ")
                if hit not in ["y", "n"]:
                    raise ValueError
            except ValueError:
                print("Sorry, please choose y or n.")
                continue
            else:
                break
        print()
        if hit == "n":
            break
        else:
            player.append(card())
            print("Your cards are: ")
            print(player)
            player_val = hand_value(player)

    #this is to indicate whether the player has busted or not
    if over(player_val):
        print("Sorry, looks like you busted, better luck next time!")
        continue

    #this checks the case of 21 as a result of an ace
    if not over(max_hand_value(player)):
        player_val = max_hand_value(player)

    #dealer hits until he busts
    while dealer_val < 16:
        dealer.append(card())
        dealer_val = hand_value(dealer)
    
    print("The dealer's cards are: ")
    print(dealer)

    #results of the game
    if over(dealer_val) or player_val > dealer_val:
        print("You win this hand!")
        balance += bet_value * 2
    elif player_val == dealer_val:
        print("It's a tie, you get your money back!")
        balance += bet_value
    else:
        print("Sorry, looks like you lost, better luck next time!")

#this is when you reach $0
print("Hope you had fun playing!")
