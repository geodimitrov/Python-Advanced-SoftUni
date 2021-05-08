
def read_input_from_text(file_name):
    with open(file_name) as file:
        return [line[:-1] for line in file.readlines()]


def count_letters_and_punctuation(line):
    letters = 0
    punc = 0

    for char in line:
        if char.isalpha():
            letters += 1

        elif char in punc_marks:
            punc += 1

    return letters, punc


def print_result(lines):
    for i in range(len(lines)):
        line_id = i + 1
        line = lines[i]
        letters_count, punctuation_count = count_letters_and_punctuation(line)
        print(f"Line {line_id}: {line} ({letters_count})({punctuation_count})")


punc_marks = ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" ]
lines = read_input_from_text("text.txt")
print_result(lines)

