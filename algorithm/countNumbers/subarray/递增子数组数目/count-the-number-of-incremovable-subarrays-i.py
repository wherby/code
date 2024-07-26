# https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/solutions/2577665/shuang-zhi-zhen-on-shi-jian-o1-kong-jian-3fl2/?envType=daily-question&envId=2024-07-10
# 移除子数组后为递增数组的数目 
from typing import List, Tuple, Optional
class Solution:
    def incremovableSubarrayCount(self, a: List[int]) -> int:
        n = len(a)
        i = 0
        while i < n - 1 and a[i] < a[i + 1]:
            i += 1
        if i == n - 1:  # 每个非空子数组都可以移除
            return n * (n + 1) // 2

        ans = i + 2  # 不保留后缀的情况，一共 i+2 个
        # 枚举保留的后缀为 a[j:]
        j = n - 1
        while j == n - 1 or a[j] < a[j + 1]:
            while i >= 0 and a[i] >= a[j]:
                i -= 1
            # 可以保留前缀 a[:i+1], a[:i], ..., a[:0] 一共 i+2 个
            ans += i + 2
            j -= 1
        return ans

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/solutions/2577665/shuang-zhi-zhen-on-shi-jian-o1-kong-jian-3fl2/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。#