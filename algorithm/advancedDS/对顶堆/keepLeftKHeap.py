# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/?envType=daily-question&envId=2026-02-02
from typing import List, Tuple, Optional
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
        self.acc -= a
    
    def rtol(self):
        
        a = self.right[0]
        self.right.remove(a)
        self.acc += a
        self.left.add(a)

    def adjust(self):
        while len(self.right) and len(self.left)< self.K:
            self.rtol()
        while  len(self.left)> self.K:
            self.ltor()

    
    def add(self, val) -> None:
        if len(self.right)>0 and val >= self.right[0]:
            self.right.add(val)
        else:
            self.left.add(val)
            self.acc+=val
        self.adjust()
    
    def delete(self,val):
        it = self.left.bisect_left(val)
        if it != len(self.left):
            self.left.remove(val)
            self.acc -=val
        else:
            self.right.remove(val)
        self.adjust

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        sl = DoubleHeap(k-1,[])
        for i in range(1,dist+2):
            sl.add(nums[i])
        ret = sl.acc
        for i in range(dist+2,n):
            sl.delete(nums[i-dist-1])
            sl.add(nums[i])
            ret = min(ret,sl.acc)
        return nums[0] + ret 
