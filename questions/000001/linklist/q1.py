#https://leetcode.cn/problems/4ueAj6/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head, insertVal: int):
        node  = Node(insertVal)
        if head is None:
            node.next = node 
            return node
        if head.next == head:
            head.next = node 
            node.next = head
            return head
        curr = head 
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node 
        node.next = next
        return head