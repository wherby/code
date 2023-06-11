#  	Time Limit Exceeded when using dictionary 
# https://leetcode.cn/contest/weekly-contest-349/problems/collecting-chocolates/submissions/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, nums, x):
        mx = sum(nums)
        n = len(nums)
        nums= nums*2
        dic = {}
        dic2 ={}
        for i in range(n):
            dic[(i,0)] = nums[i]
            dic2[(i,0)] = nums[i]
        for i in range(1,n):
            acc =0
            for j in range(n):
                dic[(j,i)]= min( dic[(j,i-1)],nums[j+i])
                acc += dic[(j,i)]
            mx = min(mx, acc + x*i)
            #print(mx,acc,i)
            
        #nums = nums[::-1]
        #print(nums)
        for i in range(1,n):
            acc=0
            for j in range(n,2*n):
                dic2[(j-n,i)] = min(dic2[(j-n,i-1)], nums[j-i])
                acc += dic2[(j-n,i)]
            mx = min(mx,acc+i*x)
            #@print(mx,acc,i)
        return mx





re =Solution().minCost([31,25,18,59],27)
print(re)