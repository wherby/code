from collections import defaultdict
class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        cnt =0
        dic1=defaultdict(list)
        dic2=defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
              tp = nums[i]+ nums[j]
              dic1[tp].append(j)
        for i in range(n):
            for j in range(i+1,n):
                tp = nums[j] - nums[i]
                dic2[tp].append(i)
        for k,v in dic1.items():
            if k in dic2:
                v2 =dic2[k]
                for t1 in v:
                    for t2 in v2:
                        if t1 < t2:
                            cnt +=1
        return cnt


nums = [1,1,1,3,5]
re = Solution().countQuadruplets(nums)
print(re)

