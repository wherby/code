from black import nullcontext


class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur =head
        ls =[]
        acc =0
        pc =ListNode(-1)
        npc =pc
        while cur:
            if acc >0 and cur.val ==0:
                ls.append(acc)
                acc =0
            else:
                acc +=cur.val
            cur = cur.next
        for a in ls:
            tp = ListNode(a)
            pc.next= tp
            pc = pc.next
        return npc.next



