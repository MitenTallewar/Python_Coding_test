"""
Implement the find max sum method that, efficiently with respect to time used,
returns the largest sum of any two elements in the given list of positive numbers.
For example, the largest sum of the list [5, 9, 7, 11] is the sum of the elements 9 and 11, which is 20.

"""
#with in built sort function
def find_max_sum(numbers):
    print("Before sorting",numbers)
    numbers.sort()
    print('After Sorting',numbers)
    x = len(numbers)-1
    y = len(numbers)-2
    ans = numbers[x] + numbers[y]
    return ans

if __name__ == "__main__":
    print(find_max_sum([5,9,7,11,10,25,35,2,1]))


#without Inbuilt Function
def find_max_sum(numbers):
    sum = 0
    max_sum =0
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

if __name__ == "__main__":
    print(find_max_sum([5,9,7,5,2,3,5]))

#with sorting
def find_max_sum(numbers):
    max_sum =0
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i] = numbers[i] + numbers[j]
                numbers[j] = numbers[i] - numbers[j]
                numbers[i] = numbers[i] - numbers[j]
    x = len(numbers)-1
    y = len(numbers)-2
    max_sum = numbers[x] + numbers[y]
    return max_sum

if __name__ == "__main__":
    print(find_max_sum([25,8,6,100]))
