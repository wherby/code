from typing import List, Tuple, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1  # 全局最大深度
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 左子树最深空节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 右子树最深空节点的深度
            if left_max_depth == right_max_depth == max_depth:  # 最深的空节点左右子树都有
                ans = node
            return max(left_max_depth, right_max_depth)  # 当前子树最深空节点的深度
        dfs(root, 0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/solutions/2428724/liang-chong-di-gui-si-lu-pythonjavacgojs-xxnk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。