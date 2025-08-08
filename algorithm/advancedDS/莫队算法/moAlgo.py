from typing import List, Tuple, Optional
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
import math
class MaxFreq():
    def __init__(self):
        self.mx = 0
        self.fdict = defaultdict(SortedList)
        self.dic = defaultdict(int)
    
    def add(self,a):
        if self.dic[a] !=0:
            self.fdict[self.dic[a]].remove(a)
        self.dic[a] +=1
        self.fdict[self.dic[a]].add(a)
        self.mx = max(self.mx,self.dic[a])
    
    def remove(self,a):
        self.fdict[self.dic[a]].remove(a)
        if len(self.fdict[self.dic[a]]) == 0 and self.mx ==self.dic[a]:
            self.mx -=1
        self.dic[a] -=1
        self.fdict[self.dic[a]].add(a)


def MoAlgo(nums,query):
    n = len(nums)
    q = len(query)
    block_size = int(math.sqrt(n)) +1

    qIndex = [(*query,i) for i,query in enumerate(query)]

    def mo_cmp(query):
        li,ri, = query[0],query[1] 
        block = li // block_size
        if block %2 == 0:
            return (block,ri)
        else:
            return (block,-ri)
    qIndex.sort(key=mo_cmp)

    mxf = MaxFreq()
    cur_li,cur_ri = 0, -1

    def modify(idx,op):
        if op ==1:
            mxf.add(nums[idx])
        else:
            mxf.remove(nums[idx])

    ret = [-1] *q

    for li, ri, threshold, idx in qIndex:
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
        if mxf.mx >= threshold:
            ret[idx] = mxf.fdict[mxf.mx][0]
    return ret


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        return MoAlgo(nums,queries)

from input.input import nums,querys
re =Solution().subarrayMajority(nums,querys)
print(len(set(nums)))
print(len(querys))
#print(re)