# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from operator import le


class Solution(object):
    def minSupplyStationNumber(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ##[zij,xuyao,buxuyao]
        def dfsNode(node):
            if node ==None:
                return [1,0,0]
            left = dfsNode(node.left)
            right = dfsNode(node.right)
            return [1 + min(left)+min(right),min(left[0],left[2])+min(right[0],right[2]),min(left[0] + min(right[0],right[2]), right[0] + min(left[0],left[2])) ]
        ret = dfsNode(root)
        return min(ret[0],ret[1] + 1, ret[2])
            





re =Solution()
print(re)