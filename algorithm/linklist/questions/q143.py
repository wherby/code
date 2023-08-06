# https://leetcode.cn/problems/reorder-list/description/

from typing import List, Tuple, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def midNode(head):
            slow= fast = head 
            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next
            return slow
        def reverseList(head):
            pre,cur = None,head
            while cur:
                nxt = cur.next 
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        mid = midNode(head)
        head2 = reverseList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 =nxt2
            