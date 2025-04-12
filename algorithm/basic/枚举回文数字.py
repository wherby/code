# 枚举N位数字 避免了奇偶性判定
# base = 10 ** ((n - 1) // 2)
# for i in range(base, base * 10):  # 枚举回文数左半边
#     s = str(i)
#     s += s[::-1][n % 2:]

# 计算组合数，先算全排列，再除去重复数量
# res = (n - cnt['0']) * fac[n - 1]
# for c in cnt.values():
#     res //= fac[c]

from math import factorial
from collections import Counter
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)
        for i in range(base, base * 10):  # 枚举回文数左半边
            s = str(i)
            s += s[::-1][n % 2:]
            if int(s) % k:  # 回文数不能被 k 整除
                continue

            sorted_s = ''.join(sorted(s))
            if sorted_s in vis:  # 不能重复统计
                continue
            vis.add(sorted_s)

            cnt = Counter(sorted_s)
            res = (n - cnt['0']) * fac[n - 1]
            for c in cnt.values():
                res //= fac[c]
            ans += res
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-count-of-good-integers/solutions/2899725/mei-ju-suo-you-hui-wen-shu-zu-he-shu-xue-3d35/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。