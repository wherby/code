from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            a = cur.val
            if cur.next:
                b = cur.next.val
                c = math.gcd(a,b)
                node = ListNode(c)
                node.next = cur.next
                cur.next = node
                cur = cur.next
            cur= cur.next 
        return head





re =Solution()
print(re)