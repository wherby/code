
from itertools import permutations
from math import inf

ODD_MASK = 0x155
D = 9

# 预处理 size 数组，详细解释见视频讲解
size = [0] * (1 << D)
for mask in range(1, 1 << D):
    t = mask & ODD_MASK
    if t & (t - 1):  # 至少有两个奇数
        continue
    for i in range(D):
        if mask >> i & 1:
            size[mask] += i + 1

class Solution:
    def specialPalindrome(self, num: int) -> int:
        target_size = len(str(num))
        ans = inf
        for mask, sz in enumerate(size):
            if sz != target_size and sz != target_size + 1:
                continue

            # 构造排列 perm
            perm = []
            odd = 0
            for x in range(1, D + 1):
                if mask >> (x - 1) & 1:
                    perm.extend([x] * (x // 2))
                    if x % 2:
                        odd = x

            # 枚举 perm 的所有排列 p，生成对应的回文数
            for p in permutations(perm):
                pal = 0
                for v in p:
                    pal = pal * 10 + v
                v = pal
                if odd:
                    pal = pal * 10 + odd
                # 反转 pal 的左半，拼在 pal 后面
                while v:
                    v, d = divmod(v, 10)
                    pal = pal * 10 + d
                if pal >= ans:  # 最优性剪枝：答案不可能变小
                    break
                if pal > num:  # 满足要求
                    ans = pal
                    break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/next-special-palindrome-number/solutions/3748548/bao-li-mei-ju-he-fa-pai-lie-by-endlessch-b5gw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。