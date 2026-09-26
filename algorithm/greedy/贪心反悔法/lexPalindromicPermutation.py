
# 在N不大的时候，有N**2 *26 的复杂度 algorithm/greedy/试填法/试填贪心法.py
# 这里的复杂度为N*26， 因为每位贪心的时候，需要判断是否前缀都相等
# 同样的题型： algorithm/greedy/贪心反悔法/lexGreaterPermutation.py

from collections import Counter
from string import ascii_letters,ascii_lowercase
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        left = Counter(s)

        def valid() -> bool:
            return all(c >= 0 for c in left.values())

        mid_ch = ''
        for ch, c in left.items():
            if c % 2 == 0:
                continue
            # s 不能有超过一个字母出现奇数次
            if mid_ch:
                return ""
            # 记录填在正中间的字母
            mid_ch = ch
            left[ch] -= 1

        n = len(s)
        # 先假设答案左半与 t 的左半（不含正中间）相同
        for i, b in enumerate(target[:n // 2]):
            left[b] -= 2

        if valid():
            # 特殊情况：把 target 左半翻转到右半，能否比 target 大？
            left_s = target[:n // 2]
            right_s = mid_ch + left_s[::-1]
            if right_s > target[n // 2:]:  # 由于左半是一样的，所以只需比右半
                return left_s + right_s

        for i in range(n // 2 - 1, -1, -1):
            b = target[i]
            left[b] += 2  # 撤销消耗
            if not valid():  # [0,i-1] 无法做到全部一样
                continue

            # 把 target[i] 增大到 j
            for j in range(ord(b) - ord('a') + 1, 26):
                ch = ascii_lowercase[j]
                if left[ch] == 0:
                    continue

                # 找到答案（下面的循环在整个算法中只会跑一次）
                left[ch] -= 2
                ans = list(target[:i + 1])
                ans[i] = ch

                # 中间可以随便填
                for ch in ascii_lowercase:
                    ans.extend(ch * (left[ch] // 2))

                # 镜像翻转
                right_s = ans[::-1]
                ans.append(mid_ch)
                ans += right_s

                return ''.join(ans)
            # 增大失败，继续枚举

        return ""

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/solutions/3821437/on-dao-xu-tan-xin-pythonjavacgo-by-endle-zips/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。