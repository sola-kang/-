import sys
from collections import deque

n = int(input())  # 풍선 개수 입력
paper = list(map(int, input().split()))  # 종이 번호 리스트

# 풍선 번호를 저장하는 deque
dq = deque(range(1, n + 1))  # 1부터 n까지의 풍선 번호
result = []  # 결과 저장           

while dq:
    balloon = dq.popleft()  #풍선 꺼내기
    result.append(balloon)  #터진풍선 저장

    move = paper[balloon-1]  #이미 터진 풍선의 종이 번호이므로 현재 풍선인덱스-1
    '''dq.remove(balloon)'''
    if move > 0 :
        for _ in range (move-1):  #양수 이동시 -1 필요
            dq.append(dq.popleft())
    else:
        for _ in range(-move):
            dq.append(dq.pop())
print(result)
        

