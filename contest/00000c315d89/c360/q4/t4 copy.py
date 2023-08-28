# https://leetcode.cn/circle/discuss/VghzJ4/
# 倍增法
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

            
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], kk: int) -> int:
        kk = kk
        n = len(receiver)
        nxt = [[0]*n for _ in range(36)]
        acc= [[0]*n for _ in range(36)]
        for i in range(n):
            acc[0][i]= receiver[i]
            nxt[0][i] = receiver[i]
        for k in range(1,36):
            for i in range(n):
                nxt[k][i]=nxt[k-1][nxt[k-1][i]]
                acc[k][i] = acc[k-1][i] + acc[k-1][nxt[k-1][i]]
        mx = 0 
        #print(acc)
        for i in range(n):
            cur = i
            tmp = i
            for k in range(36):
                if kk &(1<<(k)):
                   tmp += acc[k][cur]
                   cur = nxt[k][cur]
                   #print(i,tmp,cur,kk,kk &(1<<i),acc[k][cur],k) 
            mx = max(mx,tmp)
            #print(kk,mx)
        return mx


#re =Solution().getMaxFunctionValue(receiver =[1,0],kk=10000000000)
re =Solution().getMaxFunctionValue(receiver = [1,1,1,2,3], kk = 3)
print(re)