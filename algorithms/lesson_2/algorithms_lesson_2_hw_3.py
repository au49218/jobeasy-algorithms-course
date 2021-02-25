# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way
# until a single-digit number is produced.
# This is only applicable to the natural numbers.
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def digitsumn(number):
    str_number = str(number)
    value = 0
    while len(str_number) > 1:
        value = 0
        for i in range(len(str_number)):
            value = value + int(str_number[i])
        str_number = str(value)
    print(value)


digitsumn(16)
digitsumn(942)
digitsumn(132189)
digitsumn(493193)
