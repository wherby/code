# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==None:
            return 0
        cnt = 1
        stack = [(root.left,root.right)]
        while len(stack) >0:
            temp =[]
            for t in stack:
                if t[0] == None and t[1] ==None:
                    return cnt
                if t[0] != None:
                    temp.append((t[0].left,t[0].right))
                if t[1] != None:
                    temp.append((t[1].left,t[1].right))
            stack = temp
            cnt +=1
        return cnt