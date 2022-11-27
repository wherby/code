from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=[]
        cur = head
        while cur:
            t = cur.val
            while st and t> st[-1]:
                st.pop()
            st.append(t)
            cur = cur.next
        head = ListNode(st[0])
        cur = head
        n = len(st)
        for i in range(1,n):
            tmp  = ListNode(st[i])
            cur.next = tmp 
            cur = tmp
        return head





re =Solution()
print(re)