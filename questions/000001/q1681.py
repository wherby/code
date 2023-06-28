from typing import List, Tuple, Optional
from collections import Counter
import itertools
from functools import cache

def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        c= Counter(nums)
        for _,v in c.items():
            if v>k:
                return -1 
        n = len(nums)
        if n%k != 0:return -1
        ls= allState(n//k,n)
        dic ={}
        for state in ls:
            arr =[]
            for i in range(n):
                if (1<<i)&state:
                    arr.append(nums[i])
            if len(set(arr)) == len(arr):
                dic[state] = max(arr) - min(arr)
        @cache
        def dfs(sta):
            if sta == (1<<n)-1:
                return 0
            ret = 10**10
            for s in dic.keys():
                if s &sta == 0:
                    ret = min(ret, dic[s] + dfs(s+sta))
            return ret
        return dfs(0)

re = Solution().minimumIncompatibility(nums = [1,2,1,4], k = 2)
print(re)
                    



            