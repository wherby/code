# 倒序贪心，加上特判，如果开始的时候符合，则验证开始的情况，否则一定要找下一个？

from collections import Counter
from string import ascii_lowercase
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
        ans = list(target)
        # 先假设答案左半与 t 的左半（不含正中间）相同
        for i, b in enumerate(target[:n // 2]):
            left[b] -= 2
            ans[-1 - i] = b  # 把 target 左半翻转到右半
        # 正中间只能填那个出现奇数次的字母
        if mid_ch:
            ans[n // 2] = mid_ch

        # 把 target 左半翻转到右半，能否比 target 大？
        if valid() and (t := ''.join(ans)) > target:
            return t

        for i in range(n // 2 - 1, -1, -1):
            b = target[i]
            left[b] += 2  # 撤销消耗
            if not valid():  # [0,i-1] 无法做到全部一样
                continue

            # 把 target[i] 和 target[n-1-i] 都增大到 j
            for j in range(ord(b) - ord('a') + 1, 26):
                ch = ascii_lowercase[j]
                if left[ch] == 0:
                    continue

                # 找到答案（下面的循环在整个算法中只会跑一次）
                left[ch] -= 2
                ans[i] = ans[-1 - i] = ch
                right = ans[-1 - i:]
                del ans[i + 1:]

                # 中间的空位可以随便填
                t = []
                for ch in ascii_lowercase:
                    t.extend(ch * (left[ch] // 2))

                ans += t
                if mid_ch:
                    ans.append(mid_ch)
                ans += t[::-1]
                ans += right

                return ''.join(ans)
        return ""

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/solutions/3821437/on-dao-xu-tan-xin-pythonjavacgo-by-endle-zips/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。