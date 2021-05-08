import re


def get_words_from_text_file(file_path, expression):
    result = []

    with open(file_path) as file:
        for line in file.readlines():
            words = re.findall(expression, line)
            result.append([w.lower() for w in words])

    return result

def count_key_words(key_words, text_words):
    result = {}

    for word in key_words:
        word_count = 0
        for el in text_words:
            word_count += el.count(word)

        result[word] = word_count

    return result


def print_result(counter):

    for word, count in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print(f"{word} - {count}")


expression = "[a-zA-Z']+"
key_words = "quick is fault".split()
text_words = get_words_from_text_file("text_file.txt", expression)
word_counter = count_key_words(key_words, text_words)
print_result(word_counter)