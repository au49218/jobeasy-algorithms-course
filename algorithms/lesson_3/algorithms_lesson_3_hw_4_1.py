# CodeWars - Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.

number_list = [7, 62, 93, 29, 38, 49, 64]

result = []
for element in number_list:
    result.append(element + element)

print("Original list: " + str(number_list))
print("Double List: " + str(result))
