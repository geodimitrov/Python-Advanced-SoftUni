
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"

def find_match_brackets():
    expression = [ch for ch in input()]
    opening_brackets = []

    for i in range(len(expression)):

        if expression[i] == OPEN_BRACKET:
            opening_brackets.append(i)

        elif expression[i] == CLOSE_BRACKET:
            start = opening_brackets.pop()
            end = i + 1
            print(''.join(expression[start:end]))

find_match_brackets()
