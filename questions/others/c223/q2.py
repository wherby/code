# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dumy = ListNode(-1)
        lst =[]
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        lst[k-1],lst[-k]= lst[-k],lst[k-1]
        cur = dumy
        for n in lst:
            node = ListNode(n)
            cur.next = node
            cur = cur.next
        return dumy.next

