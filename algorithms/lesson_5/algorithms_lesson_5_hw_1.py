# When given a list, the program should return a list of all
# the elements that are below the arithmetical mean of the
# original list.  The arithmetical mean is the sum of all
# elements divided by the number of elements.


def list_mean(elements):

    result = []

    sum_elements = sum(elements)
    len_elements = len(elements)
    math_mean = sum_elements / len_elements

    for i in range(len_elements):
        if elements[i] < math_mean:
            print(elements[i])
    return math_mean


list_elements = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print(list_mean(list_elements))

