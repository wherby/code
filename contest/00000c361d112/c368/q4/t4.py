from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def getN(str):
            m = len(str)
            ret = m-1
            for j in range(m-1,0,-1):
                if m%j ==0:
                    acc = 0
                    for v in range(j):
                        s1 = [a for i,a in enumerate(str) if i %j ==v]
                        m1 = len(s1)
                        for k in range(m1//2):
                            if s1[k] !=s1[m1-1-k]:
                                acc +=1
                    #print(j,acc)
                    ret = min(ret,acc)
            #print(str,ret)
            return ret
        #getN("bcd")
        @cache
        def dfs(idx,k1):
            if idx > n:
                return 10**10
            if k1 == 0 and idx == n:
                return 0
            if k1 ==0 and idx !=n :
                return 10**8
            ret1 = n-idx-(k1-1)*2
            #print(ret1)
            ret = 10**10
            minC =""
            #print(ret,"aaa",idx,k1)
            for j in range(1,ret1+1):
                s1= s[idx:idx+j+1]
                #print(s1,getN(s1))
                if getN(s1) +dfs(idx+j+1,k1-1)< ret:
                    minC = s1
                    
                ret = min(ret, getN(s1) +dfs(idx+j+1,k1-1))
            #print(idx,k1,ret,minC ,"AA")
            return ret
        return dfs(0,k)





re =Solution().minimumChanges("acba",2)
print(re)