# https://leetcode.cn/problems/maximum-binary-tree/
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            best = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[best]:
                    best = i
        
            node = TreeNode(nums[best])
            node.left = construct(left, best - 1)
            node.right = construct(best + 1, right)
            return node
        
        return construct(0, len(nums) - 1)
