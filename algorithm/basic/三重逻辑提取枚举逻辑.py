#题目中有三重限制循环逻辑， 可以通过枚举之后 合并后两重逻辑
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c

from typing import List, Tuple, Optional

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        mx = max(arr)
        s = [0] * (mx + 2)  # cnt 数组的前缀和
        for j, y in enumerate(arr):
            for z in arr[j + 1:]:
                if abs(y - z) > b:
                    continue
                l = max(y - a, z - c, 0)
                r = min(y + a, z + c, mx)
                ans += max(s[r + 1] - s[l], 0)  # 如果 l > r + 1，s[r + 1] - s[l] 可能是负数
            for v in range(y + 1, mx + 2):
                s[v] += 1  # 把 y 加到 cnt 数组中，更新所有受到影响的前缀和
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-good-triplets/solutions/3622921/liang-chong-fang-fa-bao-li-mei-ju-qian-z-apcv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。