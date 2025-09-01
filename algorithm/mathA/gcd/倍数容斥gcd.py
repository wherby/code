# 查找所有数列对的gcd的分布
# 解决办法，从大到小遍历，找到当前数字倍增的所有值取组合，减去已经计算的倍数GCD
#  
from typing import List, Tuple, Optional
from itertools import accumulate
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt_x = [0] * (mx + 1)
        for x in nums:
            cnt_x[x] += 1

        cnt_gcd = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            c = 0
            for j in range(i, mx + 1, i):
                c += cnt_x[j]
                cnt_gcd[i] -= cnt_gcd[j]  # gcd 是 2i,3i,4i,... 的数对不能统计进来
            cnt_gcd[i] += c * (c - 1) // 2  # c 个数选 2 个，组成 c*(c-1)/2 个数对
        print(cnt_gcd)
        s = list(accumulate(cnt_gcd))  # 前缀和
        print(s)
        return [bisect_right(s, q) for q in queries]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sorted-gcd-pair-queries/solutions/2940415/mei-ju-rong-chi-qian-zhui-he-er-fen-pyth-ujis/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

ls = [2,3,4,6,8,12]
re =Solution().gcdValues(ls,[3,5,7,9])
print(re)
