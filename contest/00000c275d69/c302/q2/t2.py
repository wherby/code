class Solution:
    def maximumSum(self, nums) -> int:
        dic ={}
        mx = -1
        for num in nums:
            k = sum([int(x) for x in str(num)])
            if k not in dic:
                dic[k] =num
            else:
                mx = max(mx,num + dic[k])
                dic[k] = max(num ,dic[k])
        return mx




re =Solution()
print(re)