from typing import List, Tuple, Optional

from math import inf



class Trie:
    def __init__(self) -> None:
        self.root = [None]*2
    
    def insert(self,w):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            if r[i] ==None:
                r[i] = [None]*2
            r = r[i]
        #r.max = max(r.max,w)
        #r.min = min(r.min,w)
    
    def get(self,x,mx):
        r =self.root
        ls = '{:032b}'.format(x)
        #print(ls,len(ls),x)
        acc =0
        for idx,i in enumerate( ls):
            i = int(i)
            #print(i,r.child)
            if r[1-i] != None:
                acc += 1<<(31-idx)
                #print(31-idx,acc)
                r= r[1-i]
            else:
                r = r[i]
                if acc +1<<(31-idx)<mx:
                    return 0
        return acc

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tt  = Trie()
        mx =0
        tt.insert(nums[0])
        for a in nums[1:]:
            mx = max(mx,tt.get(a,mx))
            tt.insert(a)
        return mx
    
    

import time

start = time.time()
re =Solution().findMaximumXOR(nums)
print(re)
end = time.time()
print(end - start)