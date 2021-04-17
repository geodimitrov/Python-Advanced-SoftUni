def palindrome(word, index=0, reversed_word=""):

    if index == len(word):

        if not reversed_word == word:
            return f"{word} is not a palindrome"

        return f"{word} is a palindrome"

    else:
        reversed_word += word[-(index + 1)]
        return palindrome(word, index + 1, reversed_word)


print(palindrome("abcba"))
print(palindrome("peter"))
print(palindrome("ByyB"))