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
    def maxDifference(self, s: str, k: int) -> int:
        tar= ["0","1","2","3","4"]
        ret = -10**10
        for a1 in tar:
            for b1 in tar:
                preG = [-10**10]*4
                if a1 != b1:
                    c= Counter()
                    c2 = Counter()
                    visit={}
                    lstb1 = -1
                    left =0
                    for i,a in enumerate(s):
                        c[a] +=1
                        if i == k-1:
                            preG[0]=0
                        if a ==b1 :
                            visit[c[b1]] =i
                            ## 保证区间内一定有2个b1
                            if c[b1] >=2: 
                                lstb1  = visit[c[b1] -1]
                        if i >=k :
                            while left <= i-k and left != lstb1 and lstb1 !=-1: 
                                c2[s[left]] +=1
                                if c2[a1] %2 ==0 and c2[b1]%2 ==0:
                                    preG[0] = max(preG[0], -c2[a1] +c2[b1])
                                elif c2[a1]%2==0 and c2[b1]%2 ==1:
                                    preG[1] = max(preG[1], - c2[a1] +c2[b1])
                                elif c2[a1]%2==1 and c2[b1]%2 ==0:
                                    preG[2] = max(preG[2], -c2[a1] +c2[b1])
                                else:
                                    preG[3] = max(preG[3], -c2[a1] +c2[b1])
                                left +=1
                        if c[b1]>=2 and c[a1]>0 :
                            if c[a1]%2 == 0 and c[b1] %2 ==0 :
                                ret = max(ret, c[a1] -c[b1] +preG[2])
                            elif c[a1]%2 ==0 and c[b1] %2 ==1:
                                ret = max(ret,c[a1] -c[b1] +preG[3])
                            elif c[a1]%2==1 and c[b1] %2 ==0:
                                ret = max(ret,c[a1] -c[b1] + preG[0])
                            else:
                                ret = max(ret,c[a1] -c[b1] + preG[1])
                        #print(i,ret,preG,a1,b1,c[a1]-c[b1],c2,c)
        return ret
                    



re =Solution().maxDifference("2222130",3)
print(re)