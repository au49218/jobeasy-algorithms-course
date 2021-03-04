# Write a function to check if a number a Perfect or not

def perfect_number(pnumber):

    sum = 0
    for i in range(1, pnumber):
        if pnumber % i == 0:
            sum += i
    return sum == pnumber


number = int(input('Enter a number: '))

if perfect_number(number):
    print(f'Perfect number: {number}')
else:
    print(f'Not perfect number: {number}')
