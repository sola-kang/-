import numpy as np
from collections import deque

N = int(input())
K = int(input())
board = np.zeros((N, N), dtype=int)

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
turns = []
for _ in range(L):
    x, c = input().split()
    turns.append((int(x), c))

snake = deque([(0, 0)])  # 뱀의 머리 위치
direction = 0  # 초기 방향: 오른쪽
dx = [0, 1, 0, -1]  # 방향 변화 (오른쪽, 아래, 왼쪽, 위)
dy = [1, 0, -1, 0]  # 방향 변화 (오른쪽, 아래, 왼쪽, 위)

time = 0
turn_index = 0

while True:
    time += 1
    head_x, head_y = snake[-1]
    new_x = head_x + dx[direction]
    new_y = head_y + dy[direction]

    if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N or (new_x, new_y) in snake:
        break

    if board[new_x][new_y] == 1:
        snake.append((new_x, new_y))
        board[new_x][new_y] = 0
    else:
        snake.append((new_x, new_y))
        snake.popleft()

    if turn_index < L and time == turns[turn_index][0]:
        _, direction_change = turns[turn_index]
        if direction_change == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        turn_index += 1

print(time)