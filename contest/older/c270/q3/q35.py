# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def dfs(node, dirs,target):
            if node == None : return False
            if node.val ==target : return True

            if node.left:
                dirs.append("L")
                if dfs(node.left,dirs,target):
                    return True
                dirs.pop()
            if node.right:
                dirs.append("R")
                if dfs(node.right,dirs,target):
                    return True
                dirs.pop()
            return False
        dir1,dir2 =[],[]
        dfs(root,dir1,startValue)
        dfs(root,dir2,destValue)
        k=0
        while k < len(dir1) and k < len(dir2) and dir1[k] == dir2[k]:
            k+=1
        return "U"*(len(dir1)-k) + "".join(dir2[k:])