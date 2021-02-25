def check_length(words):
    return [word for word in words if len(word) % 2 == 0]

def print_result(filtered_words):
    return [print(word) for word in filtered_words]

words = input().split()
filtered_words = check_length(words)
print_result(filtered_words)