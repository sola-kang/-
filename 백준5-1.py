import sys
from collections import deque

left_stack = deque()
right_stack = deque()

initial = sys.stdin.readline().strip()
for char in initial:
    left_stack.append(char)

num = int(sys.stdin.readline())  #인풋대신 이걸로 수정

for _ in range(num):
    command = sys.stdin.readline().strip()
    if command == 'L':
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif command == 'B':
        if left_stack:
            left_stack.pop()
    elif command.startswith('P '):
        _, m = command.split()  #리스트 객체 생성하지 말고 필요한 부분만 추출
        left_stack.append(m)

# 결과를 문자열로 조합
result = ''.join(left_stack) + ''.join(right_stack)
print(result)
