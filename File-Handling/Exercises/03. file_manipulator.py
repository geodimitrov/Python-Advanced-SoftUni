from os import remove


def read_input():
    result = []
    while True:
        command = input()

        if command == "End":
            break
        result.append(command)

    return result


def create_new_file(file_name):
    file = open(file_name, "w")
    file.close()


def add_line_to_file(file_name, text_line):
    with open(file_name, "a") as file:
        file.write(text_line + "\n")


def replace_old_with_new_str(file_name, old_string, new_string):
    try:
        with open(file_name, "r+") as file:
            text = file.readlines()
            redacted_text = [el.replace(old_string, new_string) for el in text]
            file.seek(0)
            file.truncate(0)
            file.write("".join(redacted_text))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        remove(file_name)
    except:
        print("An error occurred")


commands = read_input()

for command in commands:

    if command.startswith("Create"):
        file_name = command.split("-")[1]
        create_new_file(file_name)

    elif command.startswith("Add"):
        file_name, text_line = command.split("-")[1:]
        add_line_to_file(file_name, text_line)

    elif command.startswith("Replace"):
        file_name, old_string, new_string = command.split("-")[1:]
        replace_old_with_new_str(file_name, old_string, new_string)

    else:
        file_name = command.split("-")[1]
        delete_file(file_name)
