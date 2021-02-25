def create_dictionary(countries, capitals):
    return {countries[i]: capitals[i] for i in range(len(countries))}

def print_result(collection):
    for key, value in collection.items():
        print(f"{key} -> {value}")

countries = input().split(", ")
capitals = input().split(", ")
dictionary = create_dictionary(countries, capitals)
print_result(dictionary)