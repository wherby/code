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
                    #print(printNode(rev),printNode(node.next),printNode(node))
                    #node.next,node,rev = rev,node.next,node
                    nodeNT = node.next
                    node.next =rev
                    nodeT =node
                    node = nodeNT
                    rev = nodeT
                    
                #prev.next.next, prev.next,prev =node,rev,prev.next
                prev.next.next = node
                prevN = prev.next
                prev.next =rev
                prev = prevN
            d += 1
        return head