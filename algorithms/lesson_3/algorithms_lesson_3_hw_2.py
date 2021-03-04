# Recursion for factorial

def recursion_factorial(fnumber):
    if fnumber == 1:
        return fnumber
    else:
        return fnumber * recursion_factorial(fnumber - 1)


number = int(input('Enter a number: '))

if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is", recursion_factorial(number))
