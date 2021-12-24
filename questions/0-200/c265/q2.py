# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        cur = head
        ls =[]
        while cur:
            ls.append(cur.val)
            cur = cur.next
        minls =[]
        maxls=[]
        n =len(ls)
        for i in range(1,n-1):
            if ls[i]< ls[i-1] and ls[i]<ls[i+1]:
                minls.append(i)
            if ls[i]>ls[i-1] and ls[i] > ls[i+1]:
                maxls.append(i)
        mmls =minls + maxls
        if len(mmls)<2:
            return [-1,-1]
        m = len(mmls)
        mmls.sort()
        mn = abs(mmls[0]-mmls[1])
        mx = mmls[-1]-mmls[0]
        for i in range(1,m):
            mn = min(mn, abs(mmls[i]-mmls[i-1]))  
        return [mn,mx]

