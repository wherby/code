# 滑动窗口维护恰好K个值
class Solution:
    def sliding_window(self, s: list[int]) -> list[list[int]]:
        res = [[0] * 26 for _ in s]

        # 计算至少有 k 种字母的子串个数
        for k in range(1, 27):
            cnt = [0] * 26
            kinds = 0
            left = 0
            for i, ch in enumerate(s):
                if cnt[ch] == 0:
                    kinds += 1
                cnt[ch] += 1
                while kinds >= k:
                    cnt[s[left]] -= 1
                    if cnt[s[left]] == 0:
                        kinds -= 1
                    left += 1
                res[i][k - 1] = left  # 右端点为 i 的合法子串个数
            if left == 0:  # 没有 k 种字母，也没有 > k 种字母，不用再算
                break

        for cnt in res:
            # (至少 j 种) - (至少 j+1 种) = (恰好 j 种)
            for j in range(25):
                if cnt[j + 1] == 0:
                    break
                cnt[j] -= cnt[j + 1]

        return res

    def countMagicalPairs(self, s: str) -> int:
        s = [ord(ch) - ord('a') for ch in s]
        pre = self.sliding_window(s)
        s.reverse()
        suf = self.sliding_window(s)  # 相当于倒着滑窗
        suf.reverse()

        ans = 0
        for i in range(len(pre) - 1):
            for p, s in zip(pre[i], suf[i + 1]):
                if p == 0 or s == 0:
                    break
                ans += p * s
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-magical-substring-pairs-ii/solutions/4048362/liang-chong-fang-fa-qia-hao-xing-hua-don-61cn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。