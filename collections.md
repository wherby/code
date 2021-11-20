# count number
import collections
count = collections.Counter(nums)

# generate bitmap of prime for a 
primes=[2,3,5,7,11,13,17,19,23,29]
mask = sum(1 <<i  for i,p in enumerate(primes) if a %p ==0)

# find index of value in array:
i = nums.index(1) 


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


# deep copy
import copy
copy.deepcopy(board)  # deep copy
copy.copy(board) # shallow copy

if want to change value ref out of function
res =[[]]
res[0] = copy.deepcopy(board)

# reduce
functools.reduce(lambda a,b : a and b ,res)
