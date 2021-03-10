def fill_list(count):
    list = []
    for _ in range(count):
        list.append(input())
    return list

n = int(input())
usernames = fill_list(n)

#use set to keep the unique usernames only
for name in set(usernames):
    print(name)