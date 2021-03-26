# Codewars: Maximum Sum Path in Two Arrays
#
# Given two sorted arrays, such that the arrays may have some
# common elements. Find the sum of the maximum sum path to reach
# from the beginning of any array to end of any of the two arrays.
# We can switch from one array to another array only at common
# elements.


def maximum_sum_path(array1, array2, m, n):

    i = 0
    j = 0
    result = 0
    sum1 = 0
    sum2 = 0

    while (i < m and j < n):

        if array1[i] < array2[j]:
            sum1 += array1[i]
            i += 1

        elif array1[i] > array2[j]:
            sum2 += array2[j]
            j += 1

        else:

            result += max(sum1, sum2)

            sum1 = 0
            sum2 = 0

            temp = i

            while i < m and array1[i] == array2[j]:
                sum1 += array1[i]
                i += 1

            while j < n and array1[temp] == array2[j]:
                sum2 += array2[j]
                j += 1

            result += max(sum1, sum2)

            sum1 = 0
            sum2 = 0

    while i < m:
        sum1 += array1[i]
        i += 1

    while j < n:
        sum2 += array2[j]
        j += 1

    result += max(sum1, sum2)

    return result


array1 = [6, 7, 11, 14, 16, 19, 34, 38]
array2 = [4, 8, 10, 11, 13, 18, 19, 21]
m = len(array1)
n = len(array2)

print("Maximum sum path: ", maximum_sum_path(array1, array2, m, n))

