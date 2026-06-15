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
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        outScope =SortedList([])
        for i,a in enumerate(nums):
            outScope.add((a,i))
        ret = -10**20
        acc = 0
        for i in range(1,k+1):
            acc += outScope[-i][0]
            ret = max(ret,acc)
        
        for i in range(n):
            inSope= SortedList([])
            outScope =SortedList([])
            gainList = SortedList([])
            for i1,a in enumerate(nums):
                outScope.add((a,i1))
            changeDic={}
            used = 0 
            curMax = 0
            for j in range(i,n):
                if j in changeDic:
                    t = changeDic[j]
                    inSope.remove((nums[j],j))
                    inSope.add((nums[t],t))
                    outScope.remove((nums[t], t))
                    used -=1
                    curMax += nums[t] -nums[j]
                    gainList.remove((nums[j]-nums[t],t,j))
                    del changeDic[j]
                else:
                    outScope.remove((nums[j],j))
                inSope.add((nums[j],j))
                curMax += nums[j]
                #print(outScope,inSope,j,i,n)
                
                while  gainList and outScope and outScope[-1][0]-inSope[0][0] > gainList[0][0]:
                    g,l,r = gainList.pop(0)
                    used -=1 
                    curMax += nums[l] - nums[r]
                    inSope.remove((nums[r],r))
                    outScope.add((nums[r],r))
                    inSope.add((nums[l],l))
                    outScope.remove((nums[l],l))
                    del changeDic[r]
                while used <k  and outScope and inSope[0][0] < outScope[-1][0] and inSope[0][0]<0:
                    used +=1
                    v1,v2 = inSope.pop(0)
                    v3,idx3 = outScope.pop()
                    inSope.add((v3,idx3))
                    outScope.add((v1,v2))
                    curMax += v3-v1 
                    changeDic[idx3] = v2
                    gainList.add((v3-v1,v2,idx3))
                ret = max(ret, curMax)
        return ret





#re =Solution().maxSum(nums = [42,-20,6,28,-14,46], k = 3)
re = Solution().maxSum([41,-7,-24,37],2)
print(re)