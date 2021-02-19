# Count odd and even digits of the whole number.
# If entered number 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_even_odd(number):
    count_even = 0
    count_odd = 0

    while number > 0:
        remainder = number % 10
        if remainder % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
        number //= 10

    print("Single - Even numbers: ", count_even)
    print("Single - Odd numbers: ", count_odd)


count_even_odd(34560)
count_even_odd(77079)


def even_odd(number_list):
    count_even = 0
    count_odd = 0

    for number in number_list:

        if number % 2 == 0:
            count_even = count_even + 1

        else:
            count_odd = count_odd + 1

    print("Multiple - Even numbers: ", count_even)
    print("Multiple - Odd numbers: ", count_odd)


number_list_array = [71, 23, 16, 47, 68, 95, 3, 5, 34, 44]
# even_odd(number_list_array)

number_list_array = [22, 23, 18, 44, 72, 92, 6, 3, 31, 75]
# even_odd(number_list_array)
