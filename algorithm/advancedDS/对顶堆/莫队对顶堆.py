# 莫队 # 对顶堆
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
import math
from bisect import bisect_right,insort_left,bisect_left

class BalancedHeap():
    def __init__(self) -> None:

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
        while len(self.left) >len(self.right):
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



def MoAlgo(nums,query,k):
    n = len(nums)
    q = len(query)
    block_size = int(math.sqrt(max(n, len(query)))) +1

    qIndex = [(*query,i) for i,query in enumerate(query)]

    def mo_cmp(query):
        li,ri, = query[0],query[1] 
        block = li // block_size
        if block %2 == 0:
            return (block,ri)
        else:
            return (block,-ri)
    qIndex.sort(key=mo_cmp)

    mxf = defaultdict(BalancedHeap)
    cur_li,cur_ri = 0, -1
    def modify(idx,op):
        if op ==1:
            mxf[nums[idx]%k].add(nums[idx]//k)
        else:
            mxf[nums[idx]%k].delete(nums[idx]//k)
    
    ssl = defaultdict(list)
    for i,a in enumerate(nums):
        ssl[a%k].append(i)
    

    ret = [-1] *q

    for li, ri, idx in qIndex:
        valIn = nums[li]% k
        lidx = bisect_left(ssl[valIn],li)
        ridx = bisect_right(ssl[valIn],ri)
        if ridx - lidx != ri-li+1:
            continue
        while cur_li > li:
            cur_li -=1
            modify(cur_li,1)
        while cur_ri < ri:
            cur_ri +=1
            modify(cur_ri,1)
        while cur_li < li:
            modify(cur_li,-1)
            cur_li +=1
        while cur_ri > ri:
            modify(cur_ri,-1)
            cur_ri -=1
        
        if len( mxf[valIn].left) + len(mxf[valIn].right) == ri-li+1:
            sl = mxf[valIn]
            t = sl.right[0]
            ret[idx] = len(sl.left)*t - sl.lacc + sl.racc -len(sl.right)*t
    return ret

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        return MoAlgo(nums,queries,k)





re =Solution().minOperations( nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]])
print(re)