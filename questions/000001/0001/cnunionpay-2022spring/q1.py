# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ast import Num
from math import fabs


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        res =[]
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        n = len(res)
        cnt =0
        def verify(start,end):
            nonlocal cnt
            if start >= end:
                return True
            if res[start] == res[end]:
                return verify(start +1 ,end-1)
            elif cnt ==0:
                cnt =1
                return verify(start,end -1) or verify(start +1,end)
            else:
                return False
        return verify(0,n-1)

re = Solution.isPalindrome() 

