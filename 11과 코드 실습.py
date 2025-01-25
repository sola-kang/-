def fib_dp_mem(n) :
    if mem[n] == None :		   # 아직 해결되지 않은 문제로 반드시 초기화
        if n < 2 :
            mem[n] = n			# 크기가 n+1 인 리스트
        else: 					
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)	
    return mem[n]

def fib_dp_tab(n) :
    f = [None] * (n+1)			# 테이블을 만들고
    f[0] = 0					# 기반 상황 처리
    f[1] = 1					# 기반 상황 처리
    for i in range(2, n + 1):	# 상향식으로: 2, 3, ... n
        f[i] = f[i-1] + f[i-2]	# 부분 문제들을 해결하고 저장함
    return f[n]					# 결과 반환

def lcs_recur(X, Y, m, n): 
    if m == 0 or n == 0: 			# 둘다 0일때
        return 0 
    elif X[m-1] == Y[n-1]: 		# 문자 같을 때
        return 1 + lcs_recur(X, Y, m-1, n-1) 
    else: 						
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n)) 
    
def lcs_dp(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)] 	
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :		# 둘중에 하나 0
                L[i][j] = 0			# 길이 0
            elif X[i-1] == Y[j-1]:	# 마지막 글자가 같으면
                L[i][j] = L[i-1][j-1]+1
            else:					# 마지막 글자가 다르면
                L[i][j] = max(L[i-1][j], L[i][j-1])

    for i in range(m+1):
        print(L[i])
    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n] 

def lcs_dp_traceback(X, Y, L):
    lcs = ""													
    i = len(X)													
    j = len(Y)													
    while i > 0 and j > 0:
        v = L[i][j] 
        if v > L[i][j-1] and v > L[i-1][j]  and v > L[i-1][j-1]: 
            i -= 1
            j -= 1
            lcs = X[i] + lcs

        elif v == L[i][j-1] and v > L[i-1][j]: j -= 1			
        else : i -= 1											

    return lcs


X = "GAME OVER"
Y = "HELLO WORLD"
print("X = ", X)
print("Y = ", Y)
print("LCS(분할 정복)", lcs_recur(X , Y, len(X), len(Y)))
print("LCS(동적 계획)", lcs_dp(X , Y) )


def knapSack_bf(W, wt, val, n): 
    if n == 0 or W == 0 :      #물건이 없거나 용량이 0
        return 0                # 그냥 0
  
    if (wt[n-1] > W):                           
        return knapSack_bf(W, wt, val, n-1)    
  
    else: 
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
        valWithout = knapSack_bf(W, wt, val, n-1)
        return max(valWith, valWithout)
    

def knapSack_dp(W, wt, val, n): 
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]   #2차원 테이블 생성
  
    for i in range(1, n + 1): 
        for w in range(1, W + 1): 
            if wt[i-1] > w:         
                A[i][w] = A[i-1][w] 
            else :                  
                valWith = val[i-1] + A[i-1][w-wt[i-1]]  
                valWithout = A[i-1][w]                  
                A[i][w] = max(valWith, valWithout)  
  
    return A[n][W]                
  

val = [60, 100, 190, 120, 200, 150] 
wt = [2, 5, 8, 4, 7, 6] 
W = 18
n = len(val) 
print("0-1배낭문제(분할 정복): ", knapSack_bf(W, wt, val, n)) 
print("0-1배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n)) 