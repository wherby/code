from typing import List, Tuple, Optional

max = lambda a, b: b if b > a else a  # 手写 max 效率更高

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        f = []

        def dfs(x: int, fa: int) -> Tuple[int, int, int]:
            f.append([0, 0])  # 用于刷表

            s = nums[x]  # 子树和
            not_inv0 = not_inv1 = 0  # 不反转 x 时的额外增量（0 表示上面反转了偶数次，1 表示上面反转了奇数次）
            for y in g[x]:
                if y == fa:
                    continue
                sy, y0, y1 = dfs(y, x)
                s += sy
                # 不反转 x，反转次数的奇偶性不变
                not_inv0 += y0
                not_inv1 += y1

            sub_res0, sub_res1 = f.pop()  # 被刷表后的结果

            # 反转 x
            # x 上面反转了偶数次，反转 x 会带来 -2 倍子树和的增量，且对于 x 的 k 级后代来说，上面反转了奇数次（所以是 sub_res1）
            inv0 = sub_res1 - s * 2
            # x 上面反转了奇数次，反转 x 会带来 2 倍子树和的增量，且对于 x 的 k 级后代来说，上面反转了偶数次（所以是 sub_res0）
            inv1 = sub_res0 + s * 2

            res0 = max(not_inv0, inv0)
            res1 = max(not_inv1, inv1)

            # 刷表法：更新 x 的 k 级祖先的状态
            if len(f) >= k:
                f[-k][0] += res0
                f[-k][1] += res1

            return s, res0, res1

        s, res0, _ = dfs(0, -1)
        return s + res0  # 对于根节点来说，上面一定反转了偶数次（0 次）

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/subtree-inversion-sum/solutions/3673852/shu-xing-dppythonjavacgo-by-endlesscheng-pjwg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。