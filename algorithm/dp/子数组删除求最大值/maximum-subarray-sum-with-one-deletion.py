# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/?envType=daily-question&envId=2024-07-21
# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6/?envType=daily-question&envId=2024-07-21
 

from typing import List, Tuple, Optional
from math import inf

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp0,dp1,mx = arr[0],-10**10,arr[0]
        for a in arr[1:]:
            dp1 = max(dp1+a, dp0)
            dp0 = max(dp0,0) + a 
            mx = max(mx,dp0,dp1)
        return mx

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        f = [[-inf] * 2] + [[0, 0] for _ in arr]
        for i, x in enumerate(arr):
            f[i + 1][0] = max(f[i][0], 0) + x
            f[i + 1][1] = max(f[i][1] + x, f[i][0])
        return max(max(r) for r in f)

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。