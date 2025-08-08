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

    query_index = [(li,ri,threshold ,i) for i,(li,ri,threshold) in enumerate(query)]

    def mo_cmp(query):
        li,ri,_,_ = query 
        block = li // block_size
        if block %2 == 0:
            return (block,ri)
        else:
            return (block,-ri)
    query_index.sort(key=mo_cmp)

    mxf = MaxFreq()
    cur_li,cur_ri = 0, -1

    ans = [-1] *q

    for li, ri, threshold, idx in query_index:
        while cur_li > li:
            cur_li -=1
            mxf.add(nums[cur_li])
        while cur_ri < ri:
            cur_ri +=1
            mxf.add(nums[cur_ri])
        while cur_li < li:
            mxf.remove(nums[cur_li])
            cur_li +=1
        while cur_ri > ri:
            mxf.remove(nums[cur_ri])
            cur_ri -=1
        if mxf.mx >= threshold:
            ans[idx] = mxf.fdict[mxf.mx][0]
    return ans


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        return MoAlgo(nums,queries)

from input.input import nums,querys
re =Solution().subarrayMajority(nums,querys)
print(len(set(nums)))
print(len(querys))
#print(re)