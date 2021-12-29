# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        idx =0
        if root:
            return True
        st = [root]
        while st:
            idx +=1
            if idx %2 ==1:
                for t in st:
                    if t.val %2 ==0:
                        return False
                n = len(st)
                for i in range(1,n):
                    if st[i].val <= st[i-1].val:
                        return False
            else:
                for t in st:
                    if t.val %2 ==1:
                        return False
                n = len(st)
                for i in range(1,n):
                    if st[i].val >= st[i-1].val:
                        return False
            tmp =[]
            n = len(st)
            for i in range(st):
                if st[i].left:
                    tmp.append(st[i].left)
                if st[i].right:
                    tmp.append(st[i].right)
            st = tmp
        return True
