from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        mx = sum(nums)
        n = len(nums)
        nums= nums*2
        dic = [[a for a in nums] for _ in range(n)]
        dic2 =[[a for a in nums] for _ in range(n)]
        #print(dic,dic2)
        for i in range(1,n):
            acc =0
            for j in range(n):
                dic[i][j]= min( dic[i-1][j],nums[j+i])
                acc += dic[i][j]
            mx = min(mx, acc + x*i)
            #print(mx,acc,i)
            
        #nums = nums[::-1]
        #print(nums)
        for i in range(1,n):
            acc=0
            for j in range(n,2*n):
                dic2[i][j-n] = min(dic2[i-1][j-n], nums[j-i])
                acc += dic2[i][j-n]
            mx = min(mx,acc+i*x)
            #@print(mx,acc,i)
        return mx





#re =Solution().minCost([31,25,18,59],27)
re =Solution().minCost([271,902,792,501,184,559,140,506,94,161],167)
print(re)