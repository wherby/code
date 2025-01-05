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
from input import nums

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        sl = [(0,0)]
        rd = {}
        dic =defaultdict(int)
        for a in nums:
            dic[a] += a
        print(dic)
        ret = -10**10
        for a in nums:
            tmp=[]
            lstMx = 0
            isSame = False
            
            cmax=ret
            for acc,b in sl:
                if b ==0:
                    lstMx = max(lstMx,acc)
                if a<0 and b ==a :
                    lstMx = max(lstMx,acc)
                    isSame =True
                if b ==a and a<0:
                    isSame =True
                    tmp.append((acc,b)) 
                else:
                    
                    d =acc +a 
                    cmax = max(cmax,d)
                    ret = max(ret,d)
                    if d <=0 :
                        if b !=0:
                            continue
                        else:
                            tmp.append((0,0))
                    else:
                        #if (d- dic[b] >=ret and b<0 ) or b ==0:
                        tmp.append((d,b))
                        # else:
                        #      print(d,dic[b],ret,b,cmax,a)
                dic[a] -=a
            if a <0 and isSame ==False and lstMx >0:
                tmp.append((lstMx,a))
            sl=tmp
            #print(len(sl))

        return ret
            
            
        




 
re =Solution().maxSubarraySum([-24,-29,45,48,-32,25,11,-7,27,-21,-38,-35,47,39,-48,-48])
print(re)