from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        leftls=[10**10]*n
        rightls = [10**10]*n
        #print("aa")
        idx = 0
        ridx = m-1
        for i in range(n):
            while idx <m:
                if s[idx] == t[i]:
                    leftls[i] =idx 
                    idx +=1
                    break
                else:
                    idx +=1
                #print(idx)
            while ridx >=0:
                if s[ridx] == t[n-1-i]:
                    rightls[n-1-i] = ridx
                    ridx-=1
                    break
                else:
                    ridx -=1
                #print(ridx)
            #print(i,idx,ridx)
        sm = n 
        ls =[]
        #print(rightls)
        for i,a in enumerate(rightls):
            ls.append([a,i])
        ls.sort()
        for i,a in enumerate(leftls):
            if a <m:
                krls = bisect_left(ls,[a+1,0])
                if krls < n:
                    #print(m,len(ls))
                    ridx,mm = ls[krls]
                    #print(ridx,mm,i,a)
                    if ridx < m:
                        sm = min(sm,max(mm-i-1,0))
                    else:
                        sm = min(sm,max(n-i-1,0))
                else:
                    sm = min(sm,n-i-1)
            else:
                krls = bisect_left(ls,[-1,10**10])
                if krls < n:
                    ridx,mm = ls[krls]
                    if ridx < n:
                        sm = min(sm,mm)
        #print(leftls,rightls,ls)
        return sm
                    
        




#re =Solution().minimumScore(s = "adebddaccdcabaade", t = "adbae")
re =Solution().minimumScore(s = "abca", t = "c")
print(re)