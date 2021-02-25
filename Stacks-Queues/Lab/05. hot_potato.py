from collections import deque

players = input().split()
step = int(input())

play_q = deque(players)

while len(play_q) > 1:
    for i in range(step - 1):
        play_q.append(play_q.popleft())
    print(f"Removed {play_q.popleft()}")

print(f"Last is {play_q.popleft()}")


