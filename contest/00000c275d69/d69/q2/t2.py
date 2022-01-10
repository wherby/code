# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ls =[]
        mx =0
        cur =head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        n = len(ls)
        for i in range(n):
            mx = max(mx,ls[i]+ ls[n-1-i])
        return mx