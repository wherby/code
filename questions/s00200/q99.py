# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def inOrder(root):
            res =[]
            if root == None:
                return res
            res= inOrder(root.left) + [root.val]+ inOrder(root.right)
            return res
        res = inOrder(root)
        res2 = sorted(res)
        cand=[]
        for i in range(len(res)):
            if res[i]  != res2[i]:
                cand.append([res[i],res2[i]])
        def change(root,v1,v2):
            if root == None:
                return
            if root.val == v1:
                root.val =v2
            elif root.val == v2:
                root.val =v1
            change(root.left,v1,v2)
            change(root.right,v1,v2)
        change(root,cand[0][0],cand[0][1])
        return root