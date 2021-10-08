# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTree(start,end):
            if start > end:
                return [None,]

            allTree  =[]
            for i in range(start,end+1):
                #print("oi")
                leftTree = generateTree(start,i-1)
                rightTree = generateTree(i+1,end)
                #print(leftTree,rightTree)

                for l in leftTree:
                    for r in rightTree:
                        currT = TreeNode(i)
                        currT.left = l
                        currT.right = r
                        allTree.append(currT)
                        #print(allTree)
            return allTree
        return generateTree(1,n) if n else []

re = Solution().generateTrees(3)
print(re)
