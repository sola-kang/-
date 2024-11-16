def sequential_search(A, key, low, high) :	
    for i in range(low, high+1) :		
        if A[i] == key :  				    
            return i 						
    return -1								



def sequential_search_transpose(A, key, low, high) :
	for i in range(low, high+1) :
		if A[i] == key :
			if i > low :		
				A[i], A[i-1] = A[i-1], A[i] 
				i = i - 1
			return i			
	return -1			




def binary_search(A, key, low, high) :
    if (low <= high) :		  
        middle = (low + high)//2
        if key == A[middle] :	
            return middle		
        elif (key<A[middle]) :	
            return binary_search(A, key, low, middle - 1)
        else :			
            return binary_search(A, key, middle + 1, high)
    return -1        		




def binary_search_iter(A, key, low, high) :
    while (low <= high) :		
        middle = (low + high)//2
        if key == A[middle]:	
            return middle
        elif (key > A[middle]):	
            low = middle + 1	
        else:			
            high = middle - 1	
    return -1        		



array = [ 3, 9, 15, 22, 31, 55, 67, 88, 91 ]
n = len(array)

print("입력배열 = ", array)
number = int(input("탐색할 숫자를 입력하시요: "))

print("순차 탐색: ", sequential_search(array, number, 0, n-1) )
print("이진 탐색: ", binary_search(array, number, 0, n-1) )
print("이진 반복: ", binary_search_iter(array, number, 0, n-1) )

class BSTNode:
    def __init__ (self, key, value):	
        self.key = key		
        self.value = value	
        self.left = None	
        self.right = None	

    def __str__(self) :
        return f"({self.key}:{self.value})"



def search_bst(n, key) :		
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key:			
        return search_bst(n.left, key)	
    else:				       
        return search_bst(n.right, key)	


def search_value_bst(n, value) :
    if n == None : return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value) 	    
    if res is not None : 
       return res
    else :				                       
       return search_value_bst(n.right, value)  

def insert_bst(root, node):
	if root == None : 			
		return node

	if node.key == root.key :	
		return root

	if node.key < root.key :
		root.left = insert_bst(root.left, node)

	else :
		root.right= insert_bst(root.right, node)

	return root							


def delete_bst (root, key) :
    if root == None :       
        return root

    if key < root.key :
        root.left = delete_bst(root.left, key)

    elif key > root.key :
        root.right= delete_bst(root.right, key)

    else : 
        if root.left== None :   
            return root.right   

        if root.right== None :  
            return root.left    


        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key                     
        root.value = succ.value                 
        root.right = delete_bst(root.right, succ.key)

    return root

def preorder(n) :
    if n is not None :
        print('{', end=' ')
        print(n, end=' ')
        preorder(n.left)
        preorder(n.right)
        print('}', end=' ')



def print_node(msg, n) :
    print(msg, n if n != None else "탐색실패")

def print_tree(msg, r) :		
    print(msg, end='')
    preorder(r)
    print()

data = [(6, "여섯"), (8, "여덟"), (2,"둘"), (4,"넷"),  (7,"일곱"), (5,"다섯"), (1,"하나"), (9,"아홉"), (3,"셋"), (0,"영")]

root = None         	       
for i in range(0, len(data)):	
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree("최초: ", root)		

n = search_bst(root, 3);        print_node("srch 3: ", n)
n = search_bst(root, 8);        print_node("srch 8: ", n)
n = search_bst(root, 0);        print_node("srch 0: ", n)
n = search_bst(root, 10);       print_node("srch10: ", n)
n = search_value_bst(root,"둘");print_node("srch둘: ", n)
n = search_value_bst(root,"열");print_node("srch열: ", n)

root = delete_bst(root, 7);     print_tree("del  7: ", root)
root = delete_bst(root, 8);     print_tree("del  8: ", root)
root = delete_bst(root, 2);     print_tree("del  2: ", root)
root = delete_bst(root, 6);     print_tree("del  6: ", root)