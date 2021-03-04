# Amicable numbers: Check if two numbers are friendly to each other or not.

number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))

sum1 = 0
sum2 = 0

for i in range(1, number1):
    if number1%i == 0:
        sum1 += i

for j in range(1, number2):
    if number2%j == 0:
        sum2 += j

if sum1 == number2 and sum2 == number1:
    print(f'Amicable numbers: {number1} and {number2}')
else:
    print(f'Not Amicable numbers: {number1} and {number2} ')
