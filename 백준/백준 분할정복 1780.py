import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minus, zero, one = 0, 0, 0   
 
def solution(x, y, N):   
    global minus, zero, one
    color = paper[x][y]    
    for i in range(x, x+N):    
        for j in range(y, y+N):
            if color != paper[i][j]:    
                for k in range(3):
                    for l in range(3):
                        solution(x+k*N//3, y+l*N//3, N//3) 
                return    
    
    if color == 0:    
        zero += 1
    elif color == 1:
        one += 1
    elif color == -1:
        minus += 1
 
solution(0, 0, N)
print(f'{minus}\n{zero}\n{one}')