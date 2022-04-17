from sortedcontainers import SortedList
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def getNumber(self, root, ops):
        """
        :type root: Optional[TreeNode]
        :type ops: List[List[int]]
        :rtype: int
        """
        ls = []
        def dfs(node):
            if node ==None:return
            dfs(node.left)
            ls.append(node.val)
            dfs(node.right)
        dfs(root)
        sls = SortedList(ls)
        ops = ops[::-1]
        res =0
        for op in ops:
            opc,x,y = tuple(op)
            idx= sls.bisect_left(x)
            #print(idx,opc,x,y,sls)
            while idx < len(sls) and y>=sls[idx]:
                if opc == 1:
                    res +=1
                sls.remove(sls[idx])
                idx= sls.bisect_left(x)
        return res