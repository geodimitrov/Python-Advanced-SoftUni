chars = input().split(", ")

dict = {char: ord(char) for char in chars}
print(dict)