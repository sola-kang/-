import sys
from collections import deque

n , m = map(int,input().split())
num_list = list(map(int,input().split()))
dq= deque()
for i in range(1, n+1):
    dq.append(i)
cnt = 0

while num_list:
    if dq[0] == num_list[0]:
        dq.popleft()
        del num_list[0]
    else :
        if dq.index(num_list[0]) > len(dq)/2: # 중간값보다 인덱스값이 크면
            while dq[0] != num_list[0]:
                dq.appendleft(dq.pop()) #후단에서 뽑아 전단에 삽입
                cnt += 1  #카운트 추가
        else :
            while dq[0] != num_list[0]:
                dq.append(dq.popleft())   #전단에서 뽑아 후단에 삽입
                cnt += 1
print(cnt)