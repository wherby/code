# 4数区间问题
class Solution(object):
    def countQuadruplets(self, nums):
        n =len(nums)
        dic = {}
        cnt =0 
        for i in range(1,n-2):
            for j in range(i):
                dic[nums[i]+nums[j]] = dic.get(nums[i] + nums[j] ,0) +1
            for j in range(i+2,n)
                if nums[j] - nums[i+1] in dic:
                    cnt += dic[nums[j]-nums[i+1]]
        return cnt


# split by t
# 1... i....  ...n
#       i+1....j
# 