#https://leetcode.com/problems/validate-binary-search-tree
class Solution(object):
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node,minVal,maxVal):
            isValid =True
            if node == None:
                return isValid       
            if node.left!=None :
                if node.left.val >= node.val:
                    isValid =False
                if minVal != None and node.left.val <=minVal:
                    isValid =False
            if node.right != None :
                if node.right.val <= node.val:
                    isValid =False
                if maxVal != None and node.right.val >= maxVal:
                    isValid =False

            return isValid and valid(node.left,minVal,node.val) and valid(node.right,node.val,maxVal)
        return valid(root,None,None)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def readTree(inTree):
    n =len(inTree)
    root = TreeNode(inTree[0])
    queue =[root]
    for i in range(1,n,2):
        node= queue.pop(0)
        if inTree[i] != None:
            left = TreeNode(inTree[i])
            node.left=left
            queue.append(left)
        if inTree[i+1] !=None:
            right = TreeNode(inTree[i+1])
            node.right=right
            queue.append(right)
    return root

inTree= [10,5,15,None,None,6,20]
root= readTree(inTree)
s=Solution()
print s.isValidBST(root)