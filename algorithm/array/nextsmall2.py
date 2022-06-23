from inspect import stack
from turtle import st


def nextSmall(A):
    # next small on the right
    n = len(A)
    right = [n]*n
    stack=[]
    for i in range(n):
        while stack and A[stack[-1]] >= A[i]:
            right[stack.pop()] = i 
        stack.append(i)
    
    # next small on the left
    left = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and A[stack[-1]] > A[i]:
            left[stack.pop()] = i 
        stack.append(i)
    print(left,right)
    
A = [2,1,3,2,1,4,2,1,4]
nextSmall(A)