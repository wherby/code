# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        isOdd =True
        st =[root]
        while st:
            next = []
            vals = []
            for k in st:
                if k != None:
                    vals.append(k.val)
                    if k.left:
                        next.append(k.left)
                    if k.right:
                        next.append(k.right)
            if isOdd:
                re = filter(lambda x : x %2 ==0,vals)
                if len(list(re)) != 0:
                    return False
                sval = list(vals)
                sval.sort()
                if vals != sval or len(set(vals)) != len(vals):
                    return False
            else:
                re = filter(lambda x : x %2 ==1,vals)
                if len(list(re)) != 0:
                    return False
                sval = list(vals)
                sval.sort(reverse= True)
                if vals != sval or len(set(vals)) != len(vals):
                    return False
            #print(vals,next)
            st = next
            isOdd = not isOdd
        return True