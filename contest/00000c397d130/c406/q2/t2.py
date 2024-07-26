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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ret =pre= ListNode()
        cur = head
        se =set(nums)
        while cur:
            if cur.val in se:
                cur=cur.next
            else:
                pre.next= cur
                pre =cur
                cur = cur.next
        pre.next = None
        return ret.next





re =Solution()
print(re)