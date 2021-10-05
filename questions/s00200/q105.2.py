
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):

        def splitLeftRight(preorder,inorder):
            v1 = preorder[0]
            k = inorder.index(v1)
            return k
        
        def builHelper(preorder,inorder):
            if len(preorder) == 0:
                return None
            k =splitLeftRight(preorder,inorder)
            root= TreeNode(preorder[0],builHelper(preorder[1:k+1],inorder[:k]),builHelper(preorder[k+1:],inorder[k+1:]))
            return root
        return builHelper(preorder,inorder)            