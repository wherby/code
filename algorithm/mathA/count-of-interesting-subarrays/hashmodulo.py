# https://leetcode.cn/contest/weekly-contest-361/problems/count-of-interesting-subarrays/
# Hash modulo counter
from typing import List, Tuple, Optional
from collections import Counter
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        curr = 0
        cnt = Counter()
        # 先统计满足 mod k = i 条件的总下标有多少个
        for num in nums:
            if num % modulo == k: curr += 1; curr %= modulo
            cnt[curr] += 1
        
        ans = 0
        curr = 0
        for num in nums:
            # 找到要找的前缀和模数
            to_find = (curr + k) % modulo
            ans += cnt[to_find]
            
            # 更新 curr
            if num % modulo == k: curr += 1; curr %= modulo
            
            # 当前位置的模数不再可以使用
            cnt[curr] -= 1
        return ans

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/ZzhMI6/view/vzX1XG/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。