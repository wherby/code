# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/2636508/python3javacgorust-yi-ti-yi-jie-di-gui-q-h6kz/?envType=daily-question&envId=2024-02-09

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None,p,q):
            return root 
        left = self.lowestCommonAncestor(root.left,p,q) 
        right = self.lowestCommonAncestor(root.right,p,q)
        return root if left and right else (left or right)