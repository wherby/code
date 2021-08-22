# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        rootDic ={}
        leafDic = {}
        for tree in trees:
            if tree.left != None:
                leafDic[tree.left.val] =1
            if tree.right != None:
                leafDic[tree.right.val] =1
            rootDic[tree.val] =[tree,1]
        for tree in trees:
            if tree.val in leafDic:
                rootDic[tree.val][1] =0

        nodes = list(filter(lambda x : x[1] !=0, rootDic.values()))
        if len(nodes) != 1:
            return None
        Root = nodes[0][0]
        queue = [(Root,-math.inf, math.inf)]
        while queue:
            temp, left,right = queue.pop()
            if not (left < temp.val < right):
                return None
            if temp.left:
                if temp.left.val in rootDic:
                    node = rootDic[temp.left.val][0]
                    temp.left =node
                    del rootDic[temp.left.val]
                queue.append((temp.left,left,temp.val))
            if temp.right:
                if temp.right.val in rootDic:
                    node = rootDic[temp.right.val][0]
                    temp.right = node
                    del rootDic[temp.right.val]
                queue.append((temp.right,temp.val,right))
        if len(rootDic) !=1:
            return None
        return Root


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

input =[TreeNode(1,None,TreeNode(3)),TreeNode(3,TreeNode(1)),TreeNode(4,TreeNode(2))]
#[TreeNode(2,TreeNode(1)),TreeNode(3,TreeNode(2),TreeNode(5)),TreeNode(5,TreeNode(4))]
a =Solution().canMerge(input)
print(a)