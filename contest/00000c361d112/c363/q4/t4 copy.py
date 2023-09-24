from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList


from collections import Counter
def getDecompositListUnderN(n):
    dic =[Counter() for _ in range(n+2)]
    visited=[False for _ in range(n+2)]
    dic[1][1] =1 
    for i in range(2,n+1):
        if visited[i]:
            continue
        for j in range(i,n+1,i):
            t= j
            visited[j] =1
            while t%i ==0:
                dic[j][i] +=1
                t = t//i
    return dic

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        n  = len(nums)
        lsDic = getDecompositListUnderN(n)
        #print(dp)
        #print(lsDic)
        for i in range(1,n+1):
            ls = lsDic[i]
            acc = 1 
            for k,v in ls.items():
                if v%2==1:
                    acc *=k
            dic[acc].append(i)
        mx = 0 
        #print(dic)
        for k,v in dic.items():
            mx = max(mx,sum([nums[i-1] for i in v ]))
        return mx





re =Solution().maximumSum(nums = [1,100,100,1])
print(re)