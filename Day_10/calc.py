from art import logo

print(logo)

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a + b

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

print(operations["*"](10, 5))

inputan = input("input some thing :")
result = eval(inputan)
# integer_result = int(result)

print(result)