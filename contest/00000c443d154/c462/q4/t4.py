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

class Solution:
    def specialPalindrome(self, n: int) -> int:
        def GetEven(n):
            return str(n)*(n//2)
        def getOdd(n):
            return str(n)*(n//2)
        
        ls = []
        for a in range(1,10):
            t = getOdd(a) + (str(a) if a%2 ==1 else "") + getOdd(a)
            ls.append(int(t))
        
        def allState(k,m):
            ret=[]
            state = (1<<k) -1
            while (state <(1<<m)):
                ret.append(state)
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
            return ret

        def getAB(a,b):
            n = a//2 +b//2
            if a//2==0:
                return []
            sts= allState(a//2,n)
            lss = []
            for st in sts:
                acc =""
                for i in range(n):
                    if (1<<i)&st:
                        acc+=str(a)
                    else:
                        acc+=str(b)
                lss.append(acc)
            return lss
        #print(getAB(2,4))
        #print(ls)
        def getABC(a,b,c):
            n = a//2 +b//2+c//2
            if a//2==0:
                return []
            sts= allState(a//2,n)
            lss = []
            for st in sts:
                acc =""
                for i in range(n):
                    if (1<<i)&st:
                        acc+=str(a)
                    else:
                        acc+=str(b)
                lss.append(acc)
            return lss

        for a in range(1,10):
            for b in range(1,10):
                if a%2 ==0 and b %2==1:
                    lss = getAB(a,b)
                    for t1 in lss:
                        t= t1 + str(b) + t1[::-1]
                        ls.append(int(t))
                    
                if a %2 ==1 and b%2 ==0:
                    lss = getAB(a,b)
                    for t1 in lss:
                        t= t1 + str(a) + t1[::-1]
                        ls.append(int(t))
                if a %2 ==0 and b%2==0 and a !=b:
                    lss = getAB(a,b)
                    for t1 in lss:
                        t= t1 + t1[::-1]
                        ls.append(int(t))

        ls.sort()
        #print(ls)
        idx =bisect_right(ls,n)
        return ls[idx]






re =Solution().specialPalindrome(682125)
print(re)