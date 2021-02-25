
def age_assignment(*names, **kwargs):
    name_age_data = kwargs
    names_ages = {}

    for name in names:
        for key in name_age_data:
            if name.startswith(key):
                names_ages[name] = name_age_data[key]
    return names_ages

print(age_assignment("Peter", "George", G=26, P=19))