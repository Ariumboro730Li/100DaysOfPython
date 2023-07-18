from caesar_functions import caesarCypherV1, caesarCypherV2, caesarCypherAngela

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

start = True
while start:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = caesarCypherV2(alphabet, text, shift, direction)
    print(f"the {direction} result is : {result} ")
    
    restart = input("Repeat the program ? y/n")
    if restart.lower() == "n":
        restart = False
