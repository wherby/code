#$https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res =[]
        stack = [root]
        i =0
        while len(stack) >0:
            cand =[]
            temp =[]
            for t in stack:
                if t == None:
                    continue
                temp.append(t.val)
                cand.append(t.left)
                cand.append(t.right)

            stack = cand

            i +=1
            if len(temp)>0:
                if i %2 ==0:
                    res.append(temp)
                else:
                    res.append(list(reversed(temp)))
        return res
