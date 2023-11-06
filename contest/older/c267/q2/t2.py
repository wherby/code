# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pcur =head
        pSeg =head
        ppre = head
        cnt = 0
        seg =2
        
        def revers(preSeg,pre,cur):
            print(preSeg.val,pre.val,cur.val)
            if preSeg.next == cur:
                return cur.next
            pre.next = cur.next
            cur.next = preSeg.next
            preSeg.next =cur
            
            return pre.next
        while pcur.next:
            cnt +=1
            ppre =pcur
            pcur =pcur.next
            if cnt ==seg:
                if seg %2 ==0:
                    pcur= revers(pSeg,ppre,pcur)
                pSeg =ppre
                seg +=1
                cnt =0
        # ppre= pcur
        # pcur =pcur.next

        # ppre= pcur
        # pcur =pcur.next
        pcur = revers(pSeg,ppre,pcur)
        print(pcur.val)
        return head


