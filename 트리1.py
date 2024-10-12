import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = list([] for _ in range(n)) # 그래프의 연결 관계 저장할 리스트
parent = [0]*n # 각각의 노드의 parent를 조사해 저장할 리스트
visited = [0]*n # 해당 노드를 방문하였는지

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(v, graph, visited):
    que = deque([v]) # 시작값을 queue에 넣기
    visited[v-1] = 1 # 방문 처리
    
    while que:
        now = que.popleft()
        for i in graph[now-1]:
            if visited[i] == 0:
                parent[i] = now # 부모노드 표시!
                que.append(i+1) # queue에 넣고
                visited[i] = 1 # 방문처리

bfs(1, graph, visited) # 트리의 루트 1이므로 여기부터 탐색 시작              
for i, ans in enumerate(parent):
    if i !=0:
        print(ans)
