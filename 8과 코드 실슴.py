def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          
    visited[s] = True               
    for v in range(len(vtx)) :      
        if adj[s][v] != 0 :         
            if visited[v]==False:   
                DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']     
edge= [[0,  1,  1,  0,  0],   
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()

from queue import Queue                 
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        
    visited = [False]*n                 
    Q = Queue()                         
    Q.put(s)                            
    visited[s] = True                   
    while not Q.empty() :
        s = Q.get()                     
        print(vtx[s], end=' ')          
        for v in aList[s] :             
            if visited[v]==False :      
                Q.put(v)                
                visited[v] = True    
                vtx = ['U','V','W','X','Y']     

aList=[[1, 2],                 
       [0, 2, 3],   
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx, aList, 0)
print()

def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               
    for v in range(len(vtx)) :      
        if adj[s][v] != 0 :         
            if visited[v]==False:  
                print("(", vtx[s], vtx[v], ")", end=' ')  
                ST_DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('ST_DFS_AM: ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()

INF = 999
def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if selected[v]==False and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj) :
    n = len(vertex)
    dist = [INF] * n		
    dist[0] = 0			   
    selected = [False] * n	

    for _ in range(n) :	
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')	
        for v in range(n) :
            if adj[u][v] != INF and not selected[v] :
                if adj[u][v]< dist[v] :	
                    dist[v] = adj[u][v]

        print(': ', dist)	#

    print()