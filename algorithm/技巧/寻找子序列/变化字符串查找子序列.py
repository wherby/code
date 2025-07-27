
class Solution:
    # 115. 不同的子序列
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        f = [1] + [0] * m
        for i, x in enumerate(s):
            for j in range(min(i, m - 1), max(m - n + i, 0) - 1, -1):
                if x == t[j]:
                    f[j + 1] += f[j]
        return f[m]

    # 计算插入 T 产生的额外 LCT 子序列个数的最大值
    def calcInsertT(self, s: str) -> int:
        cnt_t = s.count('T')  # s[i+1] 到 s[n-1] 的 'T' 的个数
        cnt_l = 0  # s[0] 到 s[i] 的 'L' 的个数
        res = 0
        for c in s:
            if c == 'T':
                cnt_t -= 1
            if c == 'L':
                cnt_l += 1
            res = max(res, cnt_l * cnt_t)
        return res

    def numOfSubsequences(self, s: str) -> int:
        extra = max(self.numDistinct(s, "CT"), self.numDistinct(s, "LC"), self.calcInsertT(s))
        return self.numDistinct(s, "LCT") + extra

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-number-of-subsequences-after-one-inserting/solutions/3734800/fu-yong-115-ti-dai-ma-qian-hou-zhui-fen-gtkqz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
re = Solution().numOfSubsequences("LCTKLCLT")
print(re)