# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def splitLeftRight(postorder,inorder):
            v1 = postorder[-1]
            k = inorder.index(v1)
            return k
        
        def builHelper(postorder,inorder):
            if len(postorder) == 0:
                return None
            k =splitLeftRight(postorder,inorder)
            print(postorder[:k],inorder[:k],postorder[k:-1],inorder[k+1:])
            root= TreeNode(postorder[-1],builHelper(postorder[:k],inorder[:k]),builHelper(postorder[k:-1],inorder[k+1:]))
            return root
        return builHelper(postorder,inorder)            