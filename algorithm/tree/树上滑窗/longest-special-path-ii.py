from typing import List, Tuple, Optional


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        g = [[] for _ in nums]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        ans = (-1, 0)
        dis = [0]
        last_depth = {}  # 颜色 -> 该颜色最近一次出现的深度 +1，注意这里已经 +1 了

        def dfs(x: int, fa: int, top_depth: int, last1: int) -> None:
            color = nums[x]
            last2 = last_depth.get(color, 0)
            top_depth = max(top_depth, min(last1, last2))  # 相较 3425 题，维护窗口左端点的逻辑变了

            nonlocal ans
            ans = max(ans, (dis[-1] - dis[top_depth], top_depth - len(dis)))

            last_depth[color] = len(dis)
            for y, w in g[x]:
                if y != fa:
                    dis.append(dis[-1] + w)
                    dfs(y, x, top_depth, max(last1, last2))  # 相较 3425 题，额外维护 last1
                    dis.pop()
            last_depth[color] = last2

        dfs(0, -1, 0, 0)
        return [ans[0], -ans[1]]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-special-path-ii/solutions/3613693/shu-shang-hua-chuang-zhi-xu-zai-3425-de-xqm73/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。