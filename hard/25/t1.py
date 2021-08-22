# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        s =[]
        t = head
        tt =  ListNode(0,head)
        head = tt
        while t:
            while len(s ) < k and t:
                x = t
                s.append(x) 
                #print(x.val)
                t = t.next
                x.next =None
            if len(s) == k :
                while len(s)>0:
                    tt.next = s.pop()
                    tt = tt.next
            else:
                for i in range(len(s)):
                    tt.next =s[i]
                    tt= tt.next
                break
        return head.next

a = ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
x=Solution().reverseKGroup(a,3)
while x:
    print(x.val)
    x=x.next
        