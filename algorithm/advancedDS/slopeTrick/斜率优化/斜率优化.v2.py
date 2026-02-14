# https://leetcode.cn/problems/minimum-partition-score/solutions/3893573/hua-fen-xing-dp-xie-lu-you-hua-tu-bao-yo-5cb0/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from itertools import accumulate
from math import inf

# 注：由于把运算封装到了单独的方法，跑得比较慢，直接把计算逻辑写在 DP 中更快
class Vec:
    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, b: "Vec") -> "Vec":
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: "Vec") -> int:
        return self.x * b.y - self.y * b.x

    def dot(self, b: "Vec") -> int:
        return self.x * b.x + self.y * b.y


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))
        f = [0] + [inf] * n

        for K in range(1, k + 1):
            new_f = [inf] * (n + 1)
            q = deque()
            
            # K 层循环中，我们要计算 new_f[i]
            # 合法的决策点 p (属于 K-1 层) 的范围是 [K-1, i-1]
            for i in range(K, n - (k - K) + 1):
                # 1. 把 p = i-1 这个属于 K-1 层的决策点入队
                # 确保计算 new_f[i] 时，决策点 p 满足 p < i
                p = i - 1
                s_p = pre[p]
                # 注意：这里必须用上一层的 f[p]
                v = Vec(s_p, f[p] + s_p * s_p - s_p)
                
                while len(q) > 1 and (q[-1] - q[-2]).det(v - q[-1]) <= 0:
                    q.pop()
                q.append(v)
                
                # 2. 查询最优决策点来更新当前层的 new_f[i]
                s_i = pre[i]
                p_query = Vec(-2 * s_i, 1)
                while len(q) > 1 and p_query.dot(q[0]) >= p_query.dot(q[1]):
                    q.popleft()
                    
                new_f[i] = p_query.dot(q[0]) + s_i * s_i + s_i
            
            f = new_f # 这一层算完了，把 new_f 给 f，供 K+1 层使用

        return f[n] // 2

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-partition-score/solutions/3893573/hua-fen-xing-dp-xie-lu-you-hua-tu-bao-yo-5cb0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。