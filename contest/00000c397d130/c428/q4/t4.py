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
from itertools import pairwise
class Solution:
    def makeStringGood(self, s: str) -> int:
        c= Counter(s)
        if len(set(c.values())) ==1:
            return 0 
        ret =len(s)
        AtoZ= 'abcdefghijklmnopqrstuvwxyz'
        vs = []
        for k,v in c.items():
            vs.append((v,k))
        ret = len(s)
        vs.sort(reverse= True)
        def minN(vs):
            #print(vs)
            n = len(vs)
            md =-1
            ret = 0
            rm =0
            if n %2 ==1:
                md = vs[n//2][0]
            else:
                a=vs[n//2-1]
                b =vs[n//2]
                if ord(a[1])-ord(b[1]) ==1:
                    rm = (a[0]-b[0]) //2
                md= (a[0]+b[0])//2
            
            ret =sum([abs(md-a[0]) for a in vs])
            print(vs,md,rm,ret)
            return ret -rm
        m = len(vs)
        acc=0
        for _ in range(m):

            ret =min(ret,minN(vs)+acc)
            t =vs.pop()
            acc +=t[0]
        #print(ret)
        return ret
        




re =Solution().makeStringGood(s = "gigigjjggjjgg")
print(re)