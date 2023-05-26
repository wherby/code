class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def testRef(slef):
        def modify(node):
            node.left=None 
            node.right=None
            node = None 
            return node

        n1 = TreeNode(10,TreeNode(1),TreeNode(2))
        modify(n1)
        print(n1.val,n1.left,n1.right)

Solution().testRef()