
try:
    with open("text.txt") as file:
        print("File found")
except:
    print("File not found")