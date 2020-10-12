

unique = []

def find_unique_numbers(numbers):
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 1:
            unique.append(numbers[i])

    return unique

print(find_unique_numbers([1,2,5,2,10]))

def find_unique_numbers(numbers):
    for i in numbers:
        if numbers.count(i) == 1:
            unique.append(i)
    return unique

print(find_unique_numbers([1,2,5,2,10]))
