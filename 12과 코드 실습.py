def hashFnStr(key) :
    sum = 0
    for c in key : 
        sum = sum + (ord(c))
    return sum % M



M = 13
table = [None]*M

def hashFn(key) :   
    return key % M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
        id = (id + 1 + M) % M  
        count -= 1         

    if count > 0 :
        table[id] = key      
    return


def lp_search(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None :  
           return None
        if table[id] != -1 and table[id] == key : 
            return table[id]    
        id = (id + 1 + M) % M   
    return None



def lp_delete(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None : return None
        if table[id] != -1 and table[id] == key : 
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1


print("   최초:", table )
lp_insert(45);  print( "45 삽입:", table )
lp_insert(27);  print( "27 삽입:", table )
lp_insert(88);  print( "88 삽입:", table )
lp_insert(9);   print( " 9 삽입:", table )

lp_insert(71);  print("71 삽입:", table )
lp_insert(60);  print("60 삽입:", table )
lp_insert(46);  print("46 삽입:", table )
lp_insert(38);  print("38 삽입:", table )
lp_insert(24);  print("24 삽입:", table )
lp_delete(60);  print("60 삭제:", table )
print("46 탐색:", lp_search(46) )






def isSafe(board, x, y):
    N = len(board)

    for i in range(y):      
        if board[i][x] == 1: return False   
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if board[i][j] == 1: return False   
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] == 1: return False  
    return True    



def solve_N_Queen(board, y):
    N = len(board)
    if y == N:                     
        printBoard(board)          
        return                    

    for x in range(N):           
        if isSafe(board, x, y):   	
            board[y][x] = 1       
            solve_N_Queen(board, y+1)
            board[y][x] = 0			


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


N = 4
board = [[0 for i in range(N)] for j in range(N)]
solve_N_Queen(board, 0)