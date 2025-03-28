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
        prev = head
        d = 2
        def printNode(node):
            if node == None:
                return "None"
            return node.val
        while prev.next:
            node, n = prev,0
            for _ in range(d):
                if not node.next:
                    break
                n+=1
                node = node.next
            if n&1:
                prev = node
            else: #reverse node 
                node,rev = prev.next,None
                for _ in range(n):
                    # node.next = rev
                    # node = node.next
                    # rev =node 
                    node.next,node,rev = rev,node.next,node
                    print(printNode(node.next),printNode(node),printNode(rev))
                prev.next.next, prev.next,prev =node,rev,prev.next
            d += 1
        return head
    