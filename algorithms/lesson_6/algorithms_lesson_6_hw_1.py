# Find the biggest number in the list (divide and rule).


def biggest_number(number_list):
    
    maximum = number_list[0]

    for i in number_list:
        if i > maximum:
            maximum = i

    return maximum


numbers_list = [15, 25, 88, 49, 21]
print("Largest number:", biggest_number(numbers_list))

