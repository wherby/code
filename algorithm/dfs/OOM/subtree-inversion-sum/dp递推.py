from typing import List, Tuple, Optional

max = lambda a, b: b if b > a else a  # 手写 max 效率更高

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> List[List[int]]:
            v = nums[x]
            res = [[v, -v] for _ in range(k)]
            s0, s1 = -v, v
            for y in g[x]:
                if y == fa:
                    continue
                fy = dfs(y, x)
                # 不反转
                for cd in range(k):
                    res[cd][0] += fy[max(cd - 1, 0)][0]
                    res[cd][1] += fy[max(cd - 1, 0)][1]
                # 反转
                s0 += fy[k - 1][1]
                s1 += fy[k - 1][0]
            # 反转
            res[0][0] = max(res[0][0], s0)
            res[0][1] = max(res[0][1], s1)
            return res

        return dfs(0, -1)[0][0]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/subtree-inversion-sum/solutions/3673852/shu-xing-dppythonjavacgo-by-endlesscheng-pjwg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。