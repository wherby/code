from string import ascii_lowercase
from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        left = Counter(s)
        for c in target:
            left[c] -= 1  # 消耗 s 中的一个字母 c

        ans = list(target)
        # 从右往左尝试
        for i in range(len(s) - 1, -1, -1):
            c = target[i]
            left[c] += 1  # 撤销消耗
            if any(cnt < 0 for cnt in left.values()):
                continue  # [0,i-1] 无法做到全部一样

            # target[i] 增大到 j
            for j in range(ord(c) - ord('a') + 1, 26):
                ch = ascii_lowercase[j]
                if left[ch] == 0:
                    continue

                left[ch] -= 1
                ans[i] = ch
                del ans[i + 1:]

                for ch in ascii_lowercase:
                    ans.extend(ch * left[ch])
                return ''.join(ans)
            # 增大失败，继续枚举
        return ""

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lexicographically-smallest-permutation-greater-than-target/solutions/3809944/dao-xu-tan-xin-pythonjavacgo-by-endlessc-fdf5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。