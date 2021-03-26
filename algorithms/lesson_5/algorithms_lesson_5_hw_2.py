# When given a list of elements find the two lowest elements.
# They can be equal to each other or different.


def list_lowest(list_number):
    lowest1 = list_number[0]
    lowest2 = None
    for i in list_number[1:]:
        if i < lowest1:
            lowest2 = lowest1
            lowest1 = i
        elif lowest2 == None or lowest2 > i:
            lowest2 = i

    print("First smallest element: ", lowest1)
    print("Second smallest element:", lowest2)


list_numbers = [15, 48, 5, 44, 34, 13, 11, 9, 7]
list_lowest(list_numbers)

