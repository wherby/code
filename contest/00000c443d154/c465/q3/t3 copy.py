from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


from typing import List, Tuple, Optional
class node:
    def __init__(self):
        self.left,self.right = None,None 

        self.mx = 0

class trie:
    def __init__(self,at):
        self.root= node()
        self.at = at

    def insert(self,i):
        curr = self.root 
        for j in range(self.at-1,-1,-1):
            if (1<<j)&i==0:
                if curr.left == None:
                    curr.left = node()
                curr= curr.left
                curr.mx = max(curr.mx,i)
            else:
                if curr.right == None:
                    curr.right = node()
                curr = curr.right
                curr.mx = max(curr.mx,i)
            j = j //2 
            #print("b",i,curr.mx)
    

    def find(self,curr, j,tar ):
        if curr == None:
            return 0 
        if j == -1:
            return curr.mx
        if (1<<j)&tar ==0:
            k = self.find(curr.right,j-1,tar)
            if k >0:
                return k 
            else:
                return self.find(curr.left,j-1,tar)
        else:
            return self.find(curr.left,j-1,tar)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = 0
        mx = max(nums)
        m = mx.bit_length()
        tre = trie(m)
        nums.sort(reverse=True)
 
        for a in nums:
            if a *mx <= ret:continue
            c =tre.find(tre.root, m-1,a)
            #print(c,a,"a")
            ret = max(ret,c*a)
            tre.insert(a)
        return ret



re =Solution().maxProduct([5,5,10,3,15,6,8])
print(re)