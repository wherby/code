# https://leetcode.cn/problems/largest-number/description/
# define new compare function in python
import functools
class Solution:
    def largestNumber(self, nums) -> str:
        def cmp(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return -1
            else:
                return 1
        nums.sort(key = functools.cmp_to_key(cmp))
        # print(nums)
        if nums[0] == 0:
            return "0"
        return "".join(map(str, nums))    

#作者：lincs
#链接：https://leetcode.cn/problems/largest-number/solutions/2250336/zi-ding-yi-pai-xu-qi-by-lincs-b7m8/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
re = Solution().largestNumber([3,30,34,5,9])
print(re)