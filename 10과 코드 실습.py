def slow_power(x, n) : 		   
    result = 1.0
    for i in range(n):			# 루브: n번 반복 0부터 니까 N번 곱해짐
        result = result * x
    return result

def power(x, n) :    #홀 짝 나눠서 구함
    if n == 0 :						
        return 1					
    elif (n % 2) == 0 :				
        return power(x*x, n//2)	
    else :							
        return x * power(x*x, (n-1)//2)	
    

import time		#테스트
print("    억지기법(2**500) =", power(2.0, 500))
print("축소정복기법(2**500) =", slow_power(2.0, 500))

t1 = time.time()
for i in range(100000) : power(2.0, 500)	
t2 = time.time()
for i in range(100000) : slow_power(2.0, 500)	
t3 = time.time()

print("    억지기법 시간... ", t3-t2)
print("축소정복기법 시간... ", t2-t1)

#정방형 행렬 m의 n 거듭제곱 multmat 함수사용
def multMat(A, B) :
    rows = len(A)
    cols = len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows): 
        for j in range(cols): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
    return result

def quick_select(A, left, right, k): 
    pos = partition(A, left, right)  #파티션 함수 사용

    if (pos+1 == left+k):				
        return A[pos] 
    elif (pos+1 > left+k):			 
        return quick_select(A, left, pos-1, k) 
    else : 						
        return quick_select(A, pos+1, right, k-(pos+1-left)) 
    
def merge_sort(A, left, right) :	    
  if left<right :			           
    mid = (left + right) // 2		
    merge_sort(A, left, mid)		
    merge_sort(A, mid + 1, right)
    merge(A, left, mid, right)

def merge(A, left, mid, right) :
    k = left			
    i = left			
    j = mid + 1			
    while i<=mid and j<=right :
        if A[i] <= A[j] :	
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :			
        sorted[k:k+right-j+1] = A[j:right+1]	
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]		

    A[left:right+1] = sorted[left:right+1]		

def fib(n) :
    if n == 0 : return 0	
    elif n == 1 : return 1	   
    else : 
        return fib(n-1) + fib(n-2)


def fib_mat(n) :
    if n == 0 : return 0      
    elif n == 1 : return 1 

    mat = [[1,1],[1,0]]        
    result = powerMat(mat, n)  
    return result[0][1]         