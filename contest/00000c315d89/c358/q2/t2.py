from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st= []
        cur = head
        while cur:
            st.append(cur.val)
            cur = cur.next
        h1=None
        curry = 0
        while st:
            a = st.pop()
            curry,a= (a*2+curry)//10,(a*2+curry)%10
            n = ListNode(a,h1)
            h1=n
        if curry:
            h1 = ListNode(curry,h1)
            
        return h1
        





re =Solution()
print(re)