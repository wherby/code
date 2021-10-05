class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSame(p,q):
            if p == None or q ==None:
                return p ==q
            return p.val == q.val and isSame(p.left,q.left) and isSame(p.right,q.right)
        return isSame(p,q)