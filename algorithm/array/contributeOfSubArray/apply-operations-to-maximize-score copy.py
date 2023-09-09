# https://leetcode.cn/problems/apply-operations-to-maximize-score/description/

# https://leetcode.cn/problems/apply-operations-to-maximize-score/solutions/2385936/gong-xian-fa-dan-diao-zhan-pythonjavacgo-23c4/

from typing import List, Tuple, Optional
MOD = 10**9+7

MX = 10**5 +1
omega = [0] * MX
for i in range(2,MX):
    if omega[i] ==0:
        for j in range(i,MX,i):
            omega[j] +=1


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n  # 质数分数 >= omega[nums[i]] 的左侧最近元素下标
        right = [n] * n  # 质数分数 >  omega[nums[i]] 的右侧最近元素下标
        st = []
        for i, v in enumerate(nums):
            while st and omega[nums[st[-1]]] < omega[v]:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)

        ans = 1
        for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda z: -z[1]):
            tot = (i - l) * (r - i)
            if tot >= k:
                ans = ans * pow(v, k, MOD) % MOD
                break
            ans = ans * pow(v, tot, MOD) % MOD
            k -= tot  # 更新剩余操作次数
        return ans

re = Solution().maximumScore([19,12,14,6,10,18],3)
print(re)