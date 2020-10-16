
def is_palindrome(word):
    words = word.lower()
    if words == words[::-1]:
        return True
    return  False


print(is_palindrome('Deleveled'))


def is_palindrome(word):
    words = word.lower()
    l = len(words) // 2
    for i in range(0,l):
        if words[i] != words[len(words)-i-1]:
            return False
    return True

print(is_palindrome('Deleveled'))

