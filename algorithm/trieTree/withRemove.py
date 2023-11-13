# https://leetcode.cn/contest/weekly-contest-371/problems/maximum-strong-pair-xor-ii/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math

from math import inf

class node:
    __slots__ ="child","max","min","is_end","cnt"
    def __init__(self) -> None:
        self.child ={}
        self.max =-inf
        self.min = inf
        self.is_end = False
        self.cnt =0

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
            r.cnt +=1
        #r.max = max(r.max,w)
        #r.min = min(r.min,w)
        r.is_end = True
    
    def remove(self,w):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            r = r.child[i]
            r.cnt -=1
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
            if 1-i  in r.child and r.child[1-i].cnt >0:
                acc += 1<<(31-idx)
                #print(31-idx,acc)
                #print(acc,x,1<<(31-idx),31-idx,1-i)
                r= r.child[1-i]
            elif i  in r.child:
                r = r.child[i]
            else:
                break
        return acc

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ret = 0
        nums.sort()
        st=deque([])
        tt = Trie()
        for a in nums:
            tt.insert(a)
            st.append(a)
            while st and st[0]*2 < a:
                b =st[0]
                tt.remove(b)
                st.popleft()
                #print(b,a)
            ret =max(ret, tt.get(a))
        return ret
        
        
        




re =Solution().maximumStrongPairXor([500,520,2500,3000])
print(re)