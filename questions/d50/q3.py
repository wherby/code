class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        n = len(nums)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i] ^ nums[i]
        pre.pop(0)
        mx =(1<<maximumBit) -1
        res = []
        #print(mx,pre)
        for i in range(n):
            res.append(mx-pre[i])
        return res[::-1]

re = Solution().getMaximumXor(nums = [2,3,4,7], maximumBit = 3)
print(re)