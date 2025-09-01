# 因为前后相等的类型是关键类型，只有分别与其他两类匹配才能得分，所以直接枚举可能的分配，求取最大值
from typing import List, Tuple, Optional
from collections import Counter
class Solution:
    # 计算除了 x 以外的出现次数之和 sum_cnt，出现次数最大值 max_cnt
    def get_sum_and_max(self, cnt: Counter, x: str) -> Tuple[int, int]:
        del cnt[x]
        sum_cnt = sum(cnt.values())
        max_cnt = max(cnt.values(), default=0)
        return sum_cnt, max_cnt

    # 计算这一组在得到 k 个 xx 后的得分
    def calc_score(self, s: int, mx: int, k: int) -> int:
        s += k
        mx = max(mx, k)
        return min(s // 2, s - mx)

    def score(self, cards: List[str], x: str) -> int:
        cnt1 = Counter(b for a, b in cards if a == x)  # 统计 "x?" 中的 ? 的出现次数
        cnt2 = Counter(a for a, b in cards if b == x)  # 统计 "?x" 中的 ? 的出现次数

        cnt_xx = cnt1[x]
        sum1, max1 = self.get_sum_and_max(cnt1, x)
        sum2, max2 = self.get_sum_and_max(cnt2, x)

        ans = 0
        # 枚举分配 k 个 xx 给第一组，其余的 xx 给第二组
        for k in range(cnt_xx + 1):
            score1 = self.calc_score(sum1, max1, k)
            score2 = self.calc_score(sum2, max2, cnt_xx - k)
            ans = max(ans, score1 + score2)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/two-letter-card-game/solutions/3768070/mei-ju-jie-lun-pythonjavacgo-by-endlessc-zbnv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。