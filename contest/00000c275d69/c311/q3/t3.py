# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        ls = [root]
        isRevers =False
        while ls:
            tmp =[]
            tmpV =[]
            for a in ls:
                tmpV.append(a.val)
                if a.left:
                    tmp.append(a.left)
                if a.right:
                    tmp.append(a.right)
            if isRevers:
                tmpV= tmpV[::-1]
                for i,b in enumerate(ls):
                    b.val = tmpV[i]
            ls = tmp
            isRevers = not isRevers
        return root




re =Solution()
print(re)