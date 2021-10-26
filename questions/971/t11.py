class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res =[]
        p = [0]
        
        def dfs(root):
            if not root:
                return []
            idx = p[0]
            if root.val != voyage[idx]:
                res.append(-1)
                return res
            p[0] +=1
            if  root.left and root.left.val != voyage[idx +1]:
                res.append(root.val)
                if root.right:
                    dfs(root.right)
                if root.left:
                    dfs(root.left)  
            else:
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
            return res
        re =dfs(root)
        for i in re:
            if i ==-1:
                return [-1]
        return re