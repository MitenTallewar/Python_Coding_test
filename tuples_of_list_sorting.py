
"""
Write a Python program to get a list, sorted in increasing order by the last element in each tuple
from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

list1 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#manual
def sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i][1] > numbers[j][1]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    return list1
print(sort(list1))


def last(n):
    return n[-1]

def sort_list(nums):
    return sorted(nums,key=last)

print(sort_list(list1))
