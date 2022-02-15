# count number
import collections
count = collections.Counter(nums)
from collections import Counter 

# generate bitmap of prime for a 
primes=[2,3,5,7,11,13,17,19,23,29]
mask = sum(1 <<i  for i,p in enumerate(primes) if a %p ==0)

# find index of value in array:
i = nums.index(1) 

# get cols of matrix  https://github.com/wherby/code/blob/master/algorithm/pythonLib/array.py
cols = list(zip(*matrix))

# header
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

# maxheap
https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
simply way is ad

# python if 

t = a*b if s[m] == "*" else a+b

# count
cnt =collections.Counter(a % 3 for a in stones)

# reduce
functools.reduce(fadd,arr1) 


# TDK bfs
q=[]
q.pop(0)
q.append(x)
```
        def bfs(start,dist, msk):
            q = [start]
            dist[start] = 0
            next= start
            while q:
                cur =q.pop(0)
                for n in g[cur]:
                    if allow[n] ==0:
                        continue
                    if dist[n] ==-1:
                        q.append(n)
                        dist[n] = dist[cur] +1
                        next =n
            return next
```
https://www.geeksforgeeks.org/deque-in-python/
same as :
from collections import deque
q = deque([1])
deque.appendleft(q,3)
deque.pop(q)

##TDK bfs visited need to updated when inqueue 
        def bfs(start):
            q =[start]
            cnt = 0
            visited[start[0]][start[1]] =1
            while q:
                t =q.pop(0)
                cnt +=1
                a,b = t[0],t[1]
                
                for x in g[a][b]:
                    if visited[x[0]][x[1]] == 0:
                        q.append(x)
                        visited[x[0]][x[1]] =1

# int to binary 把int 转换为指定的2进制
>>> a =2
>>> '{:08b}'.format(a)
'00000010'
>>> '{:032b}'.format(a) 
'00000000000000000000000000000010'
>>> bin(35)
'0b100011'
format 补0
>>> "{:02}".format(3)  
'03'

# deep copy
import copy
copy.deepcopy(board)  # deep copy
copy.copy(board) # shallow copy

if want to change value ref out of function
res =[[]]
res[0] = copy.deepcopy(board)

# reduce
functools.reduce(lambda a,b : a and b ,res)

# combination
>>> a = [1,2,3,4,5,6]
>>> import itertools
>>> ls = itertools.combinations(a,2)
>>> print(list(ls))
[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]

# permutetion
>>> a =[1,2,3]
>>> ls = itertools.permutations(a)
>>> list(ls)
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# counter 结果特殊用法
a= Counter({'a': 5})  b = Counter({'a': 3, 'b': 1})  a&b= Counter({'a': 3}) https://leetcode-cn.com/submissions/detail/245209397/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote) 
        b = Counter(magazine)
        return (a & b) == a

# sortedList 在插入的时候比用 bisect 插入快， bisect 插入的时候是O(n)
from sortedcontainers import SortedList
questions/c214/q4.py   https://leetcode-cn.com/problems/create-sorted-array-through-instructions/


# list deep copy
dp2 = list(dp1)

# dic set compare keys
```
>>> dic={"a":1,"b":2,"c":3}
>>> dic.keys()>={"a","b"}
True
>>> dic.keys()>={"a","d"}
False
>>> s1 =set(["a","b"])
>>> s2 = set(["a","b","c"])
>>> s1.issubset(s2)
True
>>> s2.issubset(s1)
False
>>> s1.issubset(dic.keys())
True
```

# choice
choice() is an inbuilt function in Python programming language that returns a random item from a list, tuple, or string. https://www.geeksforgeeks.org/python-numbers-choice-function/
# import random 
import random
  
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6] 
print(random.choice(list1))
  
# prints a random item from the string 
string = "striver" 
print(random.choice(string))  

# in a collection could easy get boarder of rectangle
        for i in range(m):
            for j in [0,n-1]:
                pos.append((i,j))
        for i in [0,m-1]:
            for j in range(1,n-1):
                pos.append((i,j))