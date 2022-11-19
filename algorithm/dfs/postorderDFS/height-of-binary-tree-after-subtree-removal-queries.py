# https://leetcode.cn/contest/weekly-contest-317/problems/height-of-binary-tree-after-subtree-removal-queries/
## https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/solutions/2759353/c-python-preoder-and-postorder-dfs/
#

from collections import defaultdict,deque
class Solution(object):
    def treeQueries(self, root, queries):
        res = defaultdict(int)

        def dfs(root, h, maxh):
            if not root: return maxh
            res[root.val] = max(res[root.val], maxh)
            root.left, root.right = root.right, root.left
            return dfs(root.right, h + 1, dfs(root.left, h + 1, max(maxh, h)))

        dfs(root, 0, 0)
        dfs(root, 0, 0)
        return [res[q] for q in queries]