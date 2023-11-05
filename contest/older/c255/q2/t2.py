class Solution:
    def findDifferentBinaryString(self, nums) :
        dic ={}
        for n in nums:
            dic[n] =1
        n = len(nums[0])
        def getStr(i,n):
            re =""
            for x in range(n):
                if i %2 ==0:
                    re = re +"0"
                else:
                    re = re +"1"
                i = i//2
            return re
        for i in range(2**n):
            str1 = getStr(i,n)
            #print(str1)
            if str1 not in dic:
                return str1
        return ""

nums = ["00","01"]
re = Solution().findDifferentBinaryString(nums)
print(re)