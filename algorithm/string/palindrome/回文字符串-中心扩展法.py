# palindrome 
# 回文字符串中心扩展
# l, r = i // 2, (i + 1) // 2  i是偶数的时候奇数个回文？i只是为了产生不同位置和不同奇偶性起点的回文
# f 多一列用来增加左右边界 f[i+1]为i长度的时候的回文长度，f[0] ==0
class Solution:
    def calc(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    f[i + 1][j] = f[i][j + 1] + 1
        mx = list(map(max, f))
        ans = max(mx) * 2  # |x| = |y| 的情况

        # 计算 |x| > |y| 的情况，中心扩展法
        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if l + 1 <= r - 1:  # s[l+1] 到 s[r-1] 是非空回文串
                ans = max(ans, r - l - 1 + mx[l + 1] * 2)
        return ans

    def longestPalindrome(self, s: str, t: str) -> int:
        return max(self.calc(s, t), self.calc(t[::-1], s[::-1]))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-palindrome-after-substring-concatenation-ii/solutions/3633596/mei-ju-hui-wen-zhong-xin-dppythonjavacgo-kpxn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。