#Write your code below this line 👇
def prime_checker(number):
    for i in range(2, 11):
        if not bool(int(number) % i):
            return "It's not a prime number"
        # print((int(number) / i))
    
    return "It's a prime number"

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
print(prime_checker(number=n))
