def runGame(the_number):
    answer = int(input("Your guess : "))
    if answer > the_number:
        print("Too High")
    elif answer < the_number:
        print("Too Low")
    else: 
        print(f"you got it, the number is {the_number}")
    
