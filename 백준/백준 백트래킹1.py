import sys
n, m = map(int, sys.stdin.readline()[:-1].split(' '))
answer = []
def pop():
    if len(answer) == m:
        return print(' '.join(map(str, answer)))
    for i in range(n):
        if i+1 not in answer:
            answer.append(i+1)
            pop()
            answer.pop()
pop()