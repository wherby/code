from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

ls =[]
for i in range(1,10**5):
    t = str(i)
    ls.append(int(t + t[::-1]))
    ls.append(int(t + t[::-1][1:]))
ls.sort()
lls =[[],[]]
for a in ls:
    lls[a%2].append(a)
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        acc = 0 
        #print(ls[:20])
        for a in nums:
            ls = lls[a%2]
            k = bisect_left(ls,a)
            l,r = k-1 ,k 
            mn = 10**10
            mn = min(mn, abs(ls[l]-a)//2)
            mn = min(mn,abs(ls[r]-a)//2)
            acc +=mn 
           # print(mn,a,l,r,ls[l],ls[r])
        return acc
                
nums = [86,295,75,598,78,200,485,119,522,788,126,481,92,820,592,892,779,525,63,823,502,282,659,467,974,395,692,912,582,140,296,541,710,481,737,37,655,37,359,196,147,407,639,462]

re =Solution().minOperations(  nums)
print(re)