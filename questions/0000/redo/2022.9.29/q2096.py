# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def search(node,val,path):
            if node == None:return False
            if node.val == val:return True
            if node.left:
                path.append("L")
                ret = search(node.left,val,path)
                if ret:
                    return True
                path.pop()
            if node.right:
                path.append("R")
                ret2 = search(node.right,val,path)
                if ret2:
                    return True
                path.pop()
            return False
        start,dest=[],[]
        search(root,startValue,start)
        search(root,destValue,dest)
        k = 0
        while len(start)> k and len(dest)>k and start[k]==dest[k]:
            k += 1
        return "U"*(len(start)-k) + "".join(dest[k:])
            
        