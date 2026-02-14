# https://leetcode.cn/problems/minimum-partition-score/solutions/3893573/hua-fen-xing-dp-xie-lu-you-hua-tu-bao-yo-5cb0/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from itertools import accumulate
from math import inf

from collections import deque
from itertools import accumulate

class Solution:
    def minPartitionScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # pre[i] 表示前 i 个元素的和
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
            
        # f[i] 表示将前 i 个元素分成 K 层后的最小分数的 2 倍
        # 初始状态：分成 0 段，只有 f[0]=0 是合法的
        f = [0] + [float('inf')] * n

        for K in range(1, k + 1):
            g = [float('inf')] * (n + 1)
            # 队列存储决策点 p 的坐标 (x, y)
            # x = pre[p]
            # y = f[p] + pre[p]^2 - pre[p]
            q = deque()
            
            # 合法的决策点 p 范围：从 K-1 到 n-1
            # 对应的被更新点 i 范围：从 K 到 n
            for i in range(K, n + 1):
                # 1. 添加入队：将 p = i-1 作为新决策点加入
                # 此时 f[p] 是上一层 (K-1) 的结果
                p = i - 1
                if f[p] != float('inf'):
                    new_x = pre[p]
                    new_y = f[p] + pre[p]**2 - pre[p]
                    
                    while len(q) >= 2:
                        x1, y1 = q[-2]
                        x2, y2 = q[-1]
                        # 维护下凸壳：判断斜率 (y2-y1)/(x2-x1) >= (new_y-y2)/(new_x-x2)
                        if (y2 - y1) * (new_x - x2) >= (new_y - y2) * (x2 - x1):
                            q.pop()
                        else:
                            break
                    q.append((new_x, new_y))
                
                # 2. 查询最优决策：当前斜率为 2 * pre[i]
                if q:
                    slope = 2 * pre[i]
                    while len(q) >= 2:
                        x1, y1 = q[0]
                        x2, y2 = q[1]
                        # 如果后面一个点更优，则弹出队首
                        # 判断：y1 - slope * x1 >= y2 - slope * x2
                        if y1 - slope * x1 >= y2 - slope * x2:
                            q.popleft()
                        else:
                            break
                    
                    best_x, best_y = q[0]
                    # 状态转移：g[i] = (y - slope * x + pre[i]^2 + pre[i])
                    g[i] = best_y - slope * best_x + pre[i]**2 + pre[i]
            
            f = g
            
        return f[n] // 2

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-partition-score/solutions/3893573/hua-fen-xing-dp-xie-lu-you-hua-tu-bao-yo-5cb0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。