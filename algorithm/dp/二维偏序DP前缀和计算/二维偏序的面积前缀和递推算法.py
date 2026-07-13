# 这里DP记录的是面积前缀和
# res = f[i + 1][j][k + 1] + f[i + 1][j + 1][k] - f[i + 1][j][k] 先假设当前点没有新增的情况下的转移算法
# 然后加上两个方向的的新增值加入前缀和



MOD = 1_000_000_007

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
                    f[j + 1] = (f[j + 1] + f[j]) % MOD
        return f[m]

    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n, m1, m2 = len(target), len(word1), len(word2)
        f = [[[0] * (m2 + 2) for _ in range(m1 + 2)] for _ in range(n + 1)]
        for j in range(1, m1 + 2):
            for k in range(1, m2 + 2):
                f[0][j][k] = 1

        for i, ch in enumerate(target):
            for j in range(m1 + 1):
                # j+k >= i+1
                for k in range(max(0, i + 1 - j), m2 + 1):
                    res = f[i + 1][j][k + 1] + f[i + 1][j + 1][k] - f[i + 1][j][k]
                    if j > 0 and word1[j - 1] == ch:
                        res += f[i][j][k + 1] - f[i][j][k]
                    if k > 0 and word2[k - 1] == ch:
                        res += f[i][j + 1][k] - f[i][j][k]
                    f[i + 1][j + 1][k + 1] = res % MOD

        return (f[n][m1 + 1][m2 + 1] - self.numDistinct(word1, target) - self.numDistinct(word2, target)) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-distinct-ways-to-form-target-from-two-strings/solutions/3991793/dong-tai-gui-hua-rong-chi-by-endlesschen-wryr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。