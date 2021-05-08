
def get_even_lines_from_text_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        result = [lines[i][:-1] for i in range(len(lines)) if i % 2 == 0]

    return result


def replace_special_chars_with_at_symbol(lines):
    for i in range(len(lines)):
        for char in special_chars:
            if char in lines[i]:
                lines[i] = lines[i].replace(char, special_symbol)


def change_word_order(lines):
    result = [line.split()[::-1] for line in lines]
    return result


def format_lines(lines):
    replace_special_chars_with_at_symbol(lines)
    result = change_word_order(lines)

    return result

def print_result(lines):
    for line in lines:
        print(" ".join(line))

special_chars = ["-", ",", ".", "!", "?"]
special_symbol = "@"
lines = get_even_lines_from_text_file("text.txt")
formatted_lines = format_lines(lines)
print_result(formatted_lines)