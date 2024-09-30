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
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dic= {}
        acc =0
        def getAllComb(tt):
            #print(tt)
            acc = 0
            ls = [0]*10
            for a in str(tt):
                ls[int(a)]+=1
            tpc = tuple(ls)
            if tpc not in dic:
                dic[tpc] =1 
                for i in range(1,10):
                    if ls[i]:
                        ls[i] -=1
                        t1 = 1
                        n1 = n-1
                        for j in range(10):
                            #print(n1,ls[j],tt)
                            t1 = t1 * math.comb(n1,ls[j])
                            n1 -= ls[j]

                            #print(n1,ls[j],"a",ls,n)

                        acc +=t1
                        ls[i]+=1
            return acc
        if n%2 ==0:
            hf = n//2-1 
            for i in range(10**hf,10**(hf+1)):
                t = str(i)
                tt = int(t+t[::-1])
                if tt%k ==0:
                    acc += getAllComb(tt)
        else:
            hf = (n+1) //2-1
            for i in range(10**hf,10**(hf+1)):
                t = str(i)
                t1=t[:-1]
                tt = int(t+t1[::-1])
                if tt%k ==0:
                    acc += getAllComb(tt)

        
                    
        return acc





re =Solution().countGoodIntegers(n = 1, k = 5)
print(re)