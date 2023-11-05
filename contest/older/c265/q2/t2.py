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
        mx =[]
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
                mx.append(i)
            if c1<p1 and c1<n1:
                mn.append(i)
        mind =1000000000000000
        if len(mn ) ==0 or len(mx) ==0:
            return [-1,-1]
        maxd = max(abs(mn[0] - mx[-1]),abs(mn[-1]- mx[0]))
        for a in mn:
            idx = bisect_left(mx,a)
            if idx >0 and idx<len(mx):
                mind = min(mind, abs(a-mx[idx]), abs(a-mn[idx-1]))
            elif idx ==0:
                mind = min(mind, abs(a-mx[idx]))
            else:
                mind = min(mind,abs(a-mx[-1]))
        return [mind,maxd]
        
