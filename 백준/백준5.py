import sys
from collections import deque
left_stack = deque()
right_stack = deque()

initial = input().strip()
for i in initial:
    left_stack.append(i)

num = int(input())

for _ in range(num):
    command = input().strip()
    if command == 'L':
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif command == 'B':
        if left_stack:
            left_stack.pop()
    elif command.startswith('P ') :
        m = command.split()[1]
        left_stack.append(m)
    
print(''.join(left_stack) + ''.join(right_stack))

