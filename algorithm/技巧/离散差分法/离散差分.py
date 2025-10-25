# 对于大值域范围的元素范围影响，可以用离散差分法
# 离散化差分的关键是找到有关差分的关键点，然后排序差分关键点
# 这里 sum_d, cnt[x] + numOperations 是两种不同情况， sum_d 是差分的值，但是差分的值和 x 又没有关系，但是这里有一个特殊的情况，x 和它的差分点是伴生关系，
# 如果 sum_d 最大的时候， cnt[x] ==0 ,则只有 numOperations， 假设cnt[x] 很大的时候，x 的前后端点差分也同时被捕获到sum_d里
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]  # 把 x 插入 diff，以保证下面能遍历到 x
            diff[x - k] += 1  # 把 [x-k,x+k] 中的每个整数的出现次数都加一
            diff[x + k + 1] -= 1

        ans = sum_d = 0
        for x, d in sorted(diff.items()):
            sum_d += d
            ans = max(ans, min(sum_d, cnt[x] + numOperations))
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-ii/solutions/2983355/liang-chong-fang-fa-chai-fen-hua-dong-ch-7buy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。