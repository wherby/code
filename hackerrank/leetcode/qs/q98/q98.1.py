class Solution(object):
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node,minVal,maxVal):        
            if node ==None:
                return True
            if node.val >=maxVal or node.val<= minVal:
                return False
            return True and valid(node.left,minVal,node.val) and valid(node.right,node.val,maxVal)
        return valid(root,float("-inf"),float("inf"))