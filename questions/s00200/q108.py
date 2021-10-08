# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)

        def helper(left,right):
            if left >right:
                return None
            k = left +(right -left) //2
            return TreeNode(nums[k],helper(left,k-1),helper(k+1,right))
        return helper(0,n-1)