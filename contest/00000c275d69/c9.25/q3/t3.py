# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lightDistribution(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dic ={}
        ret =set()
        def dfs(node):
            if node == None:
                return "*"
            left = dfs(node.left)
            right = dfs(node.right)
            hash = "(" +left  + "("+ str(node.val) +")"+ right +")"
            if hash not in dic:
                dic[hash] = node
            else:
                ret.add(dic[hash])
            return hash
        
        dfs(root)
        return list(ret)
            





re =Solution()
print(re)