# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        mn =[]
        nums =[]
        while head:
            nums.append(head.val)
            head =head.next
        n = len(nums)
        for i in range(1,n-1):
            c1 = nums[i]
            p1 =nums[i-1]
            n1 = nums[i+1]
            if c1>p1 and c1 >n1:
                mn.append(i)
            if c1<p1 and c1<n1:
                mn.append(i)
        mind =1000000000000000
        if len(mn ) <2 :
            return [-1,-1]
        maxd = mn[-1] - mn[0]
        m = len(mn)
        for i in range(1,m):
            mind = min(mind, mn[i]-mn[i-1])
        return [mind,maxd]
        
