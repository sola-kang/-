def back_tracking():
    if len(choice) == k:
        print(*choice)
        return
    for j in range(n):
        if not visited[j]:
            if choice and j+1 <= choice[-1]:
                continue
            visited[j] = True
            choice.append(j+1)
            back_tracking()
            choice.pop()
            visited[j] = False


n, k = map(int, input().split())
num_list = [i+1 for i in range(n)]
visited = [False for _ in range(n)]
choice = []
back_tracking()