#https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def helper(head,tail):
            if head == None or head == tail:
                return None
            sp =head
            fp =head
            cnt = 0
            while fp !=None and fp != tail:
                fp = fp.next
                cnt +=1
                if cnt %2 ==0:
                    sp = sp.next
            return TreeNode(sp.val,helper(head,sp),helper(sp.next,tail))
        return helper(head,None)