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

list(zip(*grid)) 矩阵列排列，列数据是tuple
>>> grid = [[3,2,1],[1,7,6],[2,7,7]]
>>> list(zip(*grid))
[(3, 1, 2), (2, 7, 7), (1, 6, 7)]

>>> grid = [[3,2,1],[1,7,6],[2,7,7]]
>>> rg= [[ls[i] for ls in grid] for i,_ in enumerate(grid)]  
>>> rg
[[3, 1, 2], [2, 7, 7], [1, 6, 7]]

https://leetcode.cn/problems/delete-columns-to-make-sorted/
class Solution(object):
    def minDeletionSize(self, strs):
        return sum(any(x>y for x,y in pairwise(col)) for col in zip(*strs))
pairwise to pair nearby value in list
```python
>>> from itertools import pairwise
>>> a =[1,2,3,4,5]
>>> pairwise(a)
<itertools.pairwise object at 0x000001ACBE2AE6E0>
>>> for a,b in pairwise(a):print(a,b)
...
1 2
2 3
3 4
4 5
>>>
```

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
reduce(xor, derived) == 0

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

小数补0
>>> n =0.1
>>> format(n,'.2f')
'0.10'
>>>
>>> a = 1001
>>> int(bin(a)[2:][::-1],2)
607

## count in iterator
>>> bin(123)      
'0b1111011'
>>> bin(123).count("1")
6
>>> "123123".count("1")
2
>>> [1,2,3,2,3,5].count(2)
2

>>> a =1023
>>> a.bit_count()
10

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
 
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2
        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))
https://leetcode.cn/problems/largest-triangle-area/

# permutetion
>>> a =[1,2,3]
>>> ls = itertools.permutations(a)
>>> list(ls)
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
>>> a =[1,1,1,1]
>>> ls = itertools.permutations(a)
>>> print(list(ls))
[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)]

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

 https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/
   https://github.com/wherby/code/blob/master/questions/000001/q1606.2.py

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


# next
>>> next((a for a in []),-1)
-1
>>> next((a for a in [1]),-1)
1

>>> any(x ==2  for x in [1,2])
True
>>> all(x==2 for x in [1,2])
False

# sum of 2d array
remains = sum(map(sum,dp0))

# chr next
nextc = lambda c : chr(ord(c)+1)
print(nextc("a"))

# count bit
https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/submissions/
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum([(665772 >> m.bit_count()) & 1 for m in range(left, right + 1)])

# sort
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=str)

## python sort with multiple index  https://leetcode-cn.com/problems/reorder-data-in-log-files/submissions/
log1.sort(key = lambda x:(x[1],x[0]))

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs

# Array manipulation
https://leetcode-cn.com/problems/projection-area-of-3d-shapes/
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 取得每列最大值的和
        zxArea = sum(map(max, grid))        # 取得每行最大值的和
        return xyArea + yzArea + zxArea

list(zip(*grid)) 矩阵列排列，列数据是tuple
>>> grid = [[3,2,1],[1,7,6],[2,7,7]]
>>> list(zip(*grid))
[(3, 1, 2), (2, 7, 7), (1, 6, 7)]

>>> grid = [[3,2,1],[1,7,6],[2,7,7]]
>>> rg= [[ls[i] for ls in grid] for i,_ in enumerate(grid)]  
>>> rg
[[3, 1, 2], [2, 7, 7], [1, 6, 7]]

# acc
```python 
from itertools import accumulate
A =[1,2,3,4]
acc1 = list(accumulate(A))
print(acc1) 
# [1, 3, 6, 10]
acc4 = list(accumulate(A, initial = 0))
print(acc4) 
#[0, 1, 3, 6, 10]
acc2 = list(accumulate(accumulate(A)))
print(acc2) 
#[1, 4, 10, 20]
acc3 = list(accumulate(accumulate(A), initial = 0))
print(acc3) 
#[0, 1, 4, 10, 20]
```

##  defaultdict of defaultdict  #defaultdict
https://stackoverflow.com/questions/5029934/defaultdict-of-defaultdict
dic2=defaultdict(lambda: defaultdict(int))

defaultdict(lambda:-10*10)

## defaultdict with sortedList for key pair 
contest\00000c275d69\c303\q3\t3.3.py
self.sl =defaultdict(lambda: SortedList(key= lambda x:(-x[0],x[1])))

## aToZ
import string
print list(string.ascii_lowercase)

small_letters = map(chr, range(ord('a'), ord('z')+1))
big_letters = map(chr, range(ord('A'), ord('Z')+1))
digits = map(chr, range(ord('0'), ord('9')+1))

ls = [chr(a) for a in range(ord('a'), ord('z')+1)]

import string
string.letters
string.uppercase
string.digits

ABC = ['abcdefghijklmnopqrstuvwxyz']

from string import ascii_lowercase   [contest/00000c275d69/c297/q4/t44.py]

isalnum() method: This method is part of Python's string manipulation capabilities.
Alphanumeric characters: These include letters (a-z, A-Z) and numbers (0-9).

## set ops

>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}

>>> a.intersection(b, c, d)
{4}

>>> a & b & c & d

## need initalize in gloabl scope to save time 
contest/00000c315d89/c358/q4/t4 copy 2.py
