


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = []
        cnt =0
        cur =head
        while cur:
            cnt +=1
            cur = cur.next
        k = cnt //2 -1
        cur = head
        while k>0:
            cur = cur.next
            k-=1
            #print(cur)
        if cnt>1:
            cur.next = cur.next.next
        if cnt ==1:
            return head.next
        return head

head= ListNode(1,  ListNode( 3,  ListNode(4, ( ListNode(7,  ListNode( 1, ( ListNode( 2, ( ListNode( 6,  None))))))))))
head =ListNode(1,None)
re =Solution().deleteMiddle(head)
print(re)
