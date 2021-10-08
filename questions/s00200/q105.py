#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/1491810/Python-stack-solution-52ms

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root  =TreeNode(preorder[0])
        stack = [root]

        i =1
        j =0

        cur = root
        while i < len(preorder):
            if cur.val == inorder[j]:
                while len(stack) >0 and stack[-1].val  == inorder[j]:
                    j+=1
                    cur = stack.pop()
                cur.right = TreeNode(preorder[i])
                cur = cur.right
            else:
                cur.left = TreeNode(preorder[i])
                cur = cur.left
            stack.append(cur)
            i+=1
        return root