def print_search_result(name, phonebook):
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

def search_contact(phonebook, n):
    for _ in range(n):
        name = input()
        print_search_result(name, phonebook)

def create_phonebook():
    phonebook = {}
    while True:
        command = input()
        if command.isdigit():
            search_contact(phonebook, int(command))
            break
        else:
            name, phone_number = command.split("-")
            phonebook[name] = phone_number

create_phonebook()