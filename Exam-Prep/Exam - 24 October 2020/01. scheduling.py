tasks = [int(el) for el in input().split(", ")]
task_index = int(input())
tasks_indices = [[tasks[i], i] for i in range(len(tasks))]
cycles = 0

for el in sorted(tasks_indices):
    cycles += el[0]
    el_index = el[1]
    if el_index == task_index:
        break
print(cycles)