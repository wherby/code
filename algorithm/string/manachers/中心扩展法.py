

class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expand(l: int, r: int) -> None:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            nonlocal ans
            ans = max(ans, r - l - 1)  # [l+1, r-1] 是回文串

        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            expand(l - 1, r)  # 删除 s[l]，继续扩展
            expand(l, r + 1)  # 删除 s[r]，继续扩展
            if ans >= n:  # 优化：提前返回答案
                return n
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-almost-palindromic-substring/solutions/3903063/zhong-xin-kuo-zhan-fa-pythonjavacgo-by-e-kmfw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
s = "a"*2498+"b"*2
re =Solution().almostPalindromic(s)
print(re)