
# https://leetcode.cn/problems/all-possible-full-binary-trees/?envType=daily-question&envId=2024-04-02
from typing import List, Tuple, Optional

from functools import cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(n: int) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode()]
            ans = []
            for i in range(n - 1):
                j = n - 1 - i
                for left in dfs(i):
                    for right in dfs(j):
                        ans.append(TreeNode(0, left, right))
            return ans

        return dfs(n)

#作者：ylb
#链接：https://leetcode.cn/problems/all-possible-full-binary-trees/solutions/2720015/python3javacgotypescript-yi-ti-yi-jie-ji-d1vm/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
re = Solution().allPossibleFBT(2)
print(re)