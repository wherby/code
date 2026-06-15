# https://leetcode.cn/problems/maximum-subarray-sum-after-at-most-k-swaps/submissions/730891591/
# 维持K大小的最小堆
from typing import List, Tuple, Optional


from sortedcontainers import SortedDict,SortedList


import math
INF  = math.inf

class BalancedHeap():
    def __init__(self,k) -> None:
        self.K= k
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
        while len(self.left) < self.K:
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
    
    def setK(self,k):
        self.K = k 
        self.adjust()
        
    

class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = max(nums)
        if len([a for a in nums if a >0]) ==0:
            return max(nums)
        if len([a for a in nums if a<0]) <=k:
            return sum([a for a in nums if a >0]) 
        for i in range(n):
            inSope = BalancedHeap(0)
            outScope = BalancedHeap(0)
            curUsed = 0
            for a in nums:
                outScope.add(-a)
            acc =0 
            for j in range(i,n):
                acc += nums[j]
                MXChange = min(j-i+1,n-(j-i+1),k)
                if curUsed > MXChange:
                    curUsed -=1 
                    inSope.setK(curUsed)
                    outScope.setK(curUsed)
                inSope.add(nums[j])

                outScope.delete(-nums[j])
                if curUsed and inSope.left[-1] + outScope.left[-1] >0:
                    curUsed -=1
                    inSope.setK(curUsed)
                    outScope.setK(curUsed)
                
                if curUsed< MXChange and len(inSope.right) and len(outScope.right) and inSope.right[0] + outScope.right[0] <0:
                    curUsed +=1 
                    inSope.setK(curUsed)
                    outScope.setK(curUsed)
                ans = max(ans, acc -(inSope.lacc +outScope.lacc))
        return ans
            





#re =Solution().maxSum(nums = [42,-20,6,28,-14,46], k = 3)
re = Solution().maxSum([41,-7,-24,37],2)
print(re)