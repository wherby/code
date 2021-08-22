class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n =0
        p = head
        while p and n <k:
            n = n+1
            p=p.next
        if n <k:
            return head
        pt = head
        pre  = None
        next =None
        cnt = 0
        while pt != None and cnt <k:
            next = pt.next
            pt.next =pre
            pre = pt
            pt =next
            cnt = cnt +1
        
        if next !=None:
            head.next =self.reverseKGroup(next,k)
        return pre