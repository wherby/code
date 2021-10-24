#https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        stack = [root]
        res =[]
        p = 0
        while stack:
            node = stack.pop()
            if node.val != voyage[p]:
                return [-1]
            if p <len(voyage) -1 and node.left:
                if node.left.val != voyage[p+1]:
                    res.append(node.val)
                    node.left,node.right = node.right,node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            p +=1
        return res
        