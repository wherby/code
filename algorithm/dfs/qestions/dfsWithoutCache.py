# https://leetcode.cn/contest/weekly-contest-337/problems/the-number-of-beautiful-subsets/
# 用暴力解法的时候dfs不能用cache

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for a in nums:
            dic[a]+=1
        keys = sorted(list(dic.keys()))
        #print(keys)
        n = len(keys)
        def dfs(idx):
            #print(state)
            if idx ==n:
                if len(state)>0:
                    return 1
                else:
                    return 0 
            c = dic[keys[idx]]
            res =0
            if keys[idx]-k not in state:
                state[keys[idx]] =1
                res +=dfs(idx+1)*((1<<c)-1)
                #print(res)
                del state[keys[idx]]
            res +=dfs(idx+1)
            return res
        state={}
        return dfs(0)
                




re =Solution().beautifulSubsets([10,4,5,7,2,1],3)
#re =Solution().beautifulSubsets(nums = [2,4,6], k = 2)
#re =Solution().beautifulSubsets([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],1)
print(re)
#print((1<<20)-1)