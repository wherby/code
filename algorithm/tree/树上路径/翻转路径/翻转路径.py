

from typing import List, Tuple, Optional

class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        g = [[] for _ in range(n)]
        for i, (x, y) in enumerate(edges):
            g[x].append((y, i))
            g[y].append((x, i))

        ans = []

        # 返回是否需要翻转 x-fa 这条边
        def dfs(x: int, fa: int) -> bool:
            rev = start[x] != target[x]  # x-fa 是否要翻转
            for y, i in g[x]:
                if y != fa and dfs(y, x):
                    ans.append(i)  # 需要翻转 y-x
                    rev = not rev  # x 被翻转了
            return rev

        if dfs(0, -1):  # 只剩下一个根节点需要翻转，无法操作
            return [-1]

        ans.sort()
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-edge-toggles-on-a-tree/solutions/3883163/dfspythonjavacgo-by-endlesscheng-5m1i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。