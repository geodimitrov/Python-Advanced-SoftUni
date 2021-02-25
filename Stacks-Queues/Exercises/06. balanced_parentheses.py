parentheses = input()

BALANCED_PAIRS = ["{}", "[]", "()"]
open_brackets = []
is_valid = True

for char in parentheses:

    if char in "{[(":
        open_brackets.append(char)
    else:
        if not open_brackets:
            is_valid = False
            break
        else:
            pair = open_brackets.pop() + char
            if pair in BALANCED_PAIRS:
                continue
            else:
                is_valid = False
                break

if is_valid and not open_brackets:
    print("YES")
else:
    print("NO")