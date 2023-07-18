from clear_terminal import clear_terminal

bidders = {}

auction = True
while auction:
    clear_terminal()
    
    name = input("What is your name ? : ")
    bid = int(input("What is your bid ? : $"))
    
    bidders[name] = bid

    any_other = input("Another bid ? (yes | no)").lower()
    if any_other == "yes":
        auction = True
    else:
        auction = False
        
the_biggest = 0
for key in bidders:
    if bidders[key] > the_biggest:
        the_biggest = bidders[key]
        the_winner = key
        
print(f"The winner is {the_winner} with bid is ${bidders[the_winner]}")