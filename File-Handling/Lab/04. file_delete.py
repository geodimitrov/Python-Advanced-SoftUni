from os import remove

try:
    remove("my_first_file.txt")
except:
    print("File already deleted")