import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
wheel = ['?'] * n 

for _ in range (k):
    s, f = input().split()
    