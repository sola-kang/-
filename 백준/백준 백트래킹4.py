N, M = map(int, input().split())

tmp_list = []

def dfs(start):

    if len(tmp_list) == M:
        for i in range(M):
            print(tmp_list[i], end=' ')
        print('')
        return

    for i in range(start,N+1):
    
        tmp_list.append(i)
        dfs(i)
        tmp_list.pop()


dfs(1)