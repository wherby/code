from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)//3
        lft = SortedList(nums[:n])
        rgh = SortedList(nums[n:])
        sm1 = sum(lft)
        sm2 = sum(rgh[-n:])
        ans = sm1 - sm2
        for i in range(n, 2*n):  #or 2*n + 1?
            idx = rgh.bisect_left(nums[i])
            if idx >= len(rgh) - n:   #
                sm2 -= nums[i]
                sm2 += rgh[-n-1]
            idx2 = lft.bisect_left(nums[i])
            if idx2 < n:
                sm1 += nums[i]
                sm1 -= lft[n-1]

            rgh.discard(nums[i])
            lft.add(nums[i])
            ans = min(ans, sm1 - sm2)

        return ans

re =Solution().minimumDifference(nums = 
print(re)