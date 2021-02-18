# Sum of 3 modified
# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

def sum_digits(number):
    total = 0
    while number > 0:
        once = number % 10
        total = total + once
        number = number // 10
    return print(total)


sum_digits(77079)
sum_digits(65623915)
sum_digits(5554712557899)
sum_digits(19)