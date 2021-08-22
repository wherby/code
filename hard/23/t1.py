from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists):
        q =[]
        head = p = ListNode()
        for l in lists:
            if l:
                heapq.heappush(q,(l.val,l))
        while len(q)>0:
            val,node = heapq.heappop(q)
            p.next=ListNode(val)
            p = p.next
            node = node.next
            if node:
                heapq.heappush(q,(node.val,node))
        return head.next

