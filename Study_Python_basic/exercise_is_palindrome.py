def is_palindrome(word):
    # 코드를 입력하세요.
    list_word = list(word)
    reversed_word = list(list_word)
    for left in range(len(list_word) // 2):
        right = len(list_word) - 1 - left
        reversed_word[right], reversed_word[left] = list_word[left], list_word[right]

    if (list_word == reversed_word):
        return True
    else:
        return False


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))


def sample(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    return True

