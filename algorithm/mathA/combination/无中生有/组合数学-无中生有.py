# https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/description/?envType=daily-question&envId=2026-09-16
# 给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。

# 请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 109 + 7 取余 后返回。

# 其实可以看做 有k 段线段，和 k+1个线段周围的可能空隔，如果直接用组合数学，线段长度不为0，空隔长度可以为0，这样就没办法组合
# 这时，把所有空隔都直接赋予1的长度，则线段和空隔的原始长度从 n-1 变为 n-1 + k-1 = n+k , 则所有被分割元素都具有一致的长度性质，只需要找到 2*k+1 个元素中 2*k个分割即可




class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, k * 2) % 1_000_000_007

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/solutions/4022747/zu-he-shu-xue-pythonjavacgo-by-endlessch-p8wu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。