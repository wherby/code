# https://leetcode.cn/contest/weekly-contest-443/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/
# 左边K个
from typing import List, Tuple, Optional


from sortedcontainers import SortedDict,SortedList




class BalancedHeap():
    def __init__(self,k) -> None:
        self.K= k//2
        self.left = SortedList([])
        self.right =SortedList([])
        self.lacc = 0
        self.racc = 0
    
    def ltor(self):
        a = self.left.pop()
        self.right.add(a)
        self.lacc -=a
        self.racc +=a
    
    def rtol(self):
        
        a = self.right[0]
        self.right.remove(a)
        self.left.add(a)
        self.racc -=a 
        self.lacc +=a 

    def adjust(self):
        while len(self.left) >self.K:
            self.ltor()
        while len(self.right) >= len(self.left)+2:
            self.rtol()
        

    
    def add(self, val) -> None:
        if len(self.right)>0 and val >= self.right[0]:
            self.right.add(val)
            self.racc +=val
        else:
            self.left.add(val)
            self.lacc +=val
        self.adjust()
    
    def delete(self,val):
        if len(self.right)>0 and val >=self.right[0]:
            self.right.remove(val)
            self.racc -=val
        else:
            self.left.remove(val)
            self.lacc -=val
        self.adjust()


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        dp2 =[10**30]*n
        acc =0
        sl = BalancedHeap(x)
        for i in range(n):
            acc += nums[i]
            sl.add(nums[i])
            if i >= x:
                sl.delete(nums[i-x])
            if i >=x-1:
                t = sl.right[0]
                dp2[i] = len(sl.left)*t - sl.lacc + sl.racc -len(sl.right)*t
        dp=list(dp2)
        for i in range(x,n):
            dp[i] =min(dp[i],dp[i-1])
        for j in range(2,k+1):
            tmp = [10**30]*n
            for i in range(x*j-1,n):
                tmp[i] = min(dp2[i] +dp[i-x],tmp[i-1])
            dp =tmp 
        return dp[-1]
            
        





re =Solution().minOperations(nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2)
print(re)