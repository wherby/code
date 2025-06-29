# https://leetcode.cn/contest/weekly-contest-456/problems/partition-array-to-minimize-xor/description/
from typing import List, Tuple, Optional


from functools import cache


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        pre = [0]
        for a in nums:
            pre.append(a^pre[-1])

        @cache
        def dfs(i,lst):
            if i < -1:
                return 10**20
            if i == -1 and lst == 0:
                return 0
            if i + 1<lst:
                return 10**20
            if i ==-1 and lst != 0:
                return 10**20
            if lst == 0 and i != 0:
                return 10**20
            ret = 10**20
            for j in range(lst-1,i+1):
                #print(lst,j)
                ns = pre[i+1] ^ pre[j]
                ret = min(ret,max(dfs(j-1,lst-1),ns))
            #print(i,lst,ret,pre)
            return ret
        n = len(nums)
        return dfs(n-1,k )


re =Solution().minXor( nums = [2,3,3,2,4]*50, k = 150)
print(re)