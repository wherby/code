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
from math import sqrt

from math import sqrt

def get_prime_factor(num):
    # 质因数分解
    res = []
    for i in range(2, int(sqrt(num)) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt:
            res.append([i, cnt])
        if i > num:
            break
    if num != 1 or not res:
        res.append([num, 1])
    return res
        
import itertools
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        ps = get_prime_factor(n)
        ls = []
        for k1,v in ps:
            ls.extend([k1]*v)
        ls.sort()
        m = len(ls)

        ret = [1]*k
        ret[0] = n
        tmp =[]
        def dfs(state,idx):
            nonlocal ret,tmp
            #print(state,idx,tmp)
            if idx ==0 and state ==0:
                if max(tmp)-min(tmp)< max(ret) - min(ret):
                    ret = list(tmp)
                return 
            if idx == 0:
                return 
            cand = []
            for i in range(m):
                if (1<<i)&state:
                    cand.append(i)
            for i in range(1,len(cand)-idx+2):
                ls1 = itertools.combinations(cand,i)
                for ls2 in ls1:
                    s1 =0
                    acc =1 
                    for b in ls2:
                        s1 += 1<<b 
                        acc = acc*ls[b]
                        tmp.append(acc)
                        dfs(state-s1,idx-1)
                        tmp.pop()
        dfs((1<<m) -1,k)
        return ret





re =Solution().minDifference(360,4)
print(re)