import sys
input = sys.stdin.readline

# 입력
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')