
# https://leetcode.cn/problems/smallest-palindromic-rearrangement-ii/solutions/3649533/shi-tian-fa-zu-he-shu-xue-pythonjavacgo-qlu6e/
from string import ascii_lowercase

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        m = n // 2

        cnt = [0] * 26
        for b in s[:m]:
            cnt[ord(b) - ord('a')] += 1

        # 为什么这样做是对的？见 62. 不同路径 我的题解
        def comb(n: int, m: int) -> int:
            m = min(m, n - m)
            res = 1
            for i in range(1, m + 1):
                res = res * (n + 1 - i) // i
                if res >= k:  # 太大了
                    return k
            return res

        # 计算长度为 sz 的字符串的排列个数
        def perm(sz: int) -> int:
            res = 1
            for c in cnt:
                if c == 0:
                    continue
                # 先从 sz 个里面选 c 个位置填当前字母
                res *= comb(sz, c)
                if res >= k:  # 太大了
                    return k
                # 从剩余位置中选位置填下一个字母
                sz -= c
            return res

        # k 太大
        if perm(m) < k:
            return ""

        # 构造回文串的左半部分
        left_s = [''] * m
        for i in range(m):
            for j in range(26):
                if cnt[j] == 0:
                    continue
                cnt[j] -= 1  # 假设填字母 j，看是否有足够的排列
                p = perm(m - i - 1)  # 剩余位置的排列个数
                if p >= k:  # 有足够的排列
                    left_s[i] = ascii_lowercase[j]
                    break
                k -= p  # k 太大，要填更大的字母（类似搜索树剪掉了一个大小为 p 的子树）
                cnt[j] += 1

        ans = left_s = ''.join(left_s)
        if n % 2:
            ans += s[n // 2]
        return ans + left_s[::-1]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/smallest-palindromic-rearrangement-ii/solutions/3649533/shi-tian-fa-zu-he-shu-xue-pythonjavacgo-qlu6e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。