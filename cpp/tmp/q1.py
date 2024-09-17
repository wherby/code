
"""
given A= [d + i*a for i in range(N)]
Let b= d + i*a [i in range(N+1)] and let B =[b* i ] 
Maximize C=len(A &B) and find max value of b 
"""

# O(N^2)
def func1(A,d,a):
    sm = 0 
    ret =[]
    for b in A:
        acc = 0 
        for c in A: 
            if c %b ==0:
                acc +=1
        if acc >= sm:
            sm = acc 
            ret = [b,sm]
    return ret

# O(NlogN)
def func2(A,d,a):
    sm = 0
    ret = []

    for b in A:
        acc = 0
        for c in range(b,A[-1]+1,b):
            if (c-d)%a == 0:
                acc +=1
        if acc >= sm:
            sm = acc 
            ret = [b,sm]
    return ret

# O(CN)
def func3(A,d,a):
    sm = 0
    ret = []
    dic ={}
    Find = False
    for b in A:
        if Find ==True:break
        acc = 0
        for c in range(b,A[-1]+1,b):
            if c in dic:
                Find = True
                break
            dic[c] =1
            if (c-d)%a == 0:
                acc +=1
        if acc >= sm:
            sm = acc 
            ret = [b,sm]
    return ret


# How to get O(C) algorithim?
'''
    Let's find some facts:

    1. A[0] == d is a greedy answer for find C
    
    2. If C == 1, the maximun of b is A[-1]
       if C >1, then the maximun value of b should be  in d and d + LCM(d,a), then we could binary search the value.  
    
'''







A = [1 + 2*i for i in range(21)]
print(func1(A,1,2))
print(func2(A,1,2))
print(func3(A,1,2))
A =[8 +9*i for i in range(5)]

print(func3(A,8,9))












