# will timeout
from typing import List, Tuple, Optional

from math import inf

class node:
    __slots__ ="child","max","min","is_end"
    def __init__(self) -> None:
        self.child ={}
        self.max =-inf
        self.min = inf
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = node()
    
    def insert(self,w):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            if i not in r.child:
                r.child[i] = node()
            r = r.child[i]
        #r.max = max(r.max,w)
        #r.min = min(r.min,w)
        r.is_end = True
    
    def get(self,x):
        r =self.root
        if len(r.child) == 0:
            return -1
        ls = '{:032b}'.format(x)
        #print(ls,len(ls),x)
        acc =0
        for idx,i in enumerate( ls):
            i = int(i)
            #print(i,r.child)
            if 1-i  in r.child:
                acc += 1<<(31-idx)
                #print(31-idx,acc)
                r= r.child[1-i]
            else:
                r = r.child[i]
        return acc

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tt  = Trie()
        mx =0
        tt.insert(nums[0])
        for a in nums[1:]:
            mx = max(mx,tt.get(a))
            tt.insert(a)
        return mx
    
    

import time

start = time.time()
re =Solution().findMaximumXOR(nums)
print(re)
end = time.time()
print(end - start)