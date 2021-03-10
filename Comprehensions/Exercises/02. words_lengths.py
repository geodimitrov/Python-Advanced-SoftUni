def print_result(collection):
    result = [f"{key} -> {value}" for key, value in collection.items()]
    print(*result, sep=", ")

words = input().split(", ")

words_lengths = {word: len(word) for word in words}
print_result(words_lengths)