seq = []
n_queries = int(input())

for q in range(n_queries):
    command = input()

    if command.startswith("1"):
        element = int(command.split()[1])
        seq.append(element)
    elif command.startswith("2"):
        if seq:
            seq.pop()
    elif command.startswith("3"):
        if seq:
            print(max(seq))
    elif command.startswith("4"):
        if seq:
            print(min(seq))

print(*reversed(seq), sep=", ")