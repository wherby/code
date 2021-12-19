class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        MOD = 10**9+7
        nums.append(0)
        st = [-1]
        res = 0
        presums = [0]
        for x in nums:
            presums.append(presums[-1]+x)
        for i, x in enumerate(nums):
            while nums[st[-1]] > x:
                cur = nums[st.pop()]
                res = max(res, cur*(presums[i]-presums[st[-1]+1]))
            st.append(i)
        return res%MOD