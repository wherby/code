# 对顶堆
from sortedcontainers import SortedList


class DoubleHeap():
    def __init__(self,k,arr) -> None:
        self.K= k
        self.left = SortedList(arr)
        self.right =SortedList([])
        self.acc = 0
    
    def ltor(self):
        a = self.left.pop()
        self.right.add(a)
        self.acc += a[0]*a[1] # acc update
    
    def rtol(self):
        
        a = self.right[0]
        self.right.remove(a)
        self.acc -= a[0]*a[1] # acc update
        self.left.add(a)

    def adjust(self):
        while len(self.left) and len(self.right)< self.K:
            self.ltor()
        while len(self.right) and len(self.right)> self.K:
            self.rtol()

    
    def add(self, val) -> None:
        if len(self.right)>0 and val >= self.right[0]:
            self.right.add(val)
            self.acc += val[0]*val[1] # acc update
        else:
            self.left.add(val)
        self.adjust()
    
    def delete(self,val):
        it = self.left.bisect_left(val)
        if it != len(self.left):
            self.left.remove(val)
        else:
            self.right.remove(val)
            self.acc -= val[0]*val[1]  # acc update
        self.adjust

from typing import List, Tuple, Optional
from collections import Counter
## keep K item in self.right

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        arr =[]
        for a in nums:
            arr.append((0,a))
        dp = DoubleHeap(x,arr)
        c =Counter()
        #print(dp.left,dp.right)
        for i,a in enumerate(nums):
            c[a] +=1
            #print(dp.left,dp.right,i,a)
            dp.delete((c[a]-1,a))
            dp.add((c[a],a))
            if i>=k:
                b = nums[i-k]
                c[b] -=1
                dp.delete((c[b]+1,b))
                dp.add((c[b],b))
            if i >=k-1:
                ret.append(dp.acc)
        return ret
    
re =Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)
print(re)
