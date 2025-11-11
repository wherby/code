# https://leetcode.com/contest/biweekly-contest-169/problems/count-subarrays-with-majority-element-ii/
# 使用前缀和方式获取子数组统计分布，
from typing import List, Tuple, Optional


class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]+ (1 if nums[i] == target else -1)

        vals = sorted(set(pre))
        valsDict = {v:i for i,v in enumerate(vals)}
        m = len(vals)

        ft = FenwickTree([0]*(m+1))
        ft.add(valsDict[0],1)

        ans = 0 
        for i in range(n):
            idx = valsDict[pre[i+1]]
            if idx > 0:
                ans += ft.sumTo(idx-1)
            ft.add(idx,1)
        return ans




re =Solution().countMajoritySubarrays(nums = [1,2,2,3], target = 2)
print(re)