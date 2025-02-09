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
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:

        n = len(target)

        lss=[]
        
        def dfs(state,ls):
            if state ==(1<<n)-1:
                return lss.append(list(ls))
            ret = 10**10
            for i in range(1,2<<(n-1)):
                if i&state ==0 :
                    ls.append(i)
                    dfs(i|state,ls) 
                    ls.pop()
        dfs(0,[])
        res =10**10
        nm = list(nums)
        @cache
        def getLCM(state):
            lcm = 1
            for i in range(n):
                if state &(1<<i):
                    lcm = math.lcm(lcm,target[i-1])
            st = SortedList([])
            for i,a in enumerate(nums):
                t = (lcm - a%lcm)%lcm
                st.add((t,i))
                if len(st)>4:
                    st.pop()
            return ([a[1] for a in st],lcm)
        used =defaultdict(int)
        def dfs2(idx):
            if idx ==m:
                #print(nums,"*")
                return 0
            ret = 10**10
            for a in cand[idx]:
                t1= (lcms[idx] - nums[a] %lcms[idx])%lcms[idx]
                if t1 >0 and used[a]>0:
                    continue
                used[a] +=1
                nums[a] +=t1 
                ret = min(ret,t1 +dfs2(idx+1))
                used[a] -=1
                nums[a] -=t1 
            return ret
        for ls in lss:
            m = len(ls)
            cand =[]
            lcms= []
            for a in ls:
                cad,lcm= getLCM(a)
                cand.append(cad)
                lcms.append(lcm)
            #print(cand,lcms)
            res =min(res, dfs2(0))
            #print(ls,dfs2(0))
        return res
            
            
            




re =Solution().minimumIncrements(nums = [8,10,9], target = [10,6,6])
print(re)