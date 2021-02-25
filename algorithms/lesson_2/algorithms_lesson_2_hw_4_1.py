# CodeWars - Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.

def SumOfPositive(numbers):
    sumpositive = 0
    for i in numbers:
        if i > 0:
            sumpositive = sumpositive + i
    print(sumpositive)


SumOfPositive([-1, 1, -2, 2])
SumOfPositive([-1, 3, -2, 0])
SumOfPositive([-1, -3, -2, 1])
