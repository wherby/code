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
    def __init__(self):
        self.root= node()

    def insert(self,i):
        curr = self.root 
        j = i
        while j:
            if j%2 ==0:
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
    

    def find(self,curr, j ):
        if curr == None:
            return 0 
        if j == 0:
            return curr.mx
        if j %2 ==0:

            return max(self.find(curr.right,j//2),self.find(curr.left,j//2))
        else:
            return self.find(curr.left,j//2)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = 0
        nums.sort()
        tre = trie()
        nums.sort(reverse=True)
        # for a in nums:
        #     tre.insert(a)
        for a in nums:
            c =tre.find(tre.root, a)
            #print(c,a,"a")
            ret = max(ret,c*a)
            #print("d",tre.find())
            tre.insert(a)
        return ret



re =Solution().maxProduct([5,5,10,3,15,6,8])
print(re)