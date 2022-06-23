class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums = nums[::-1]
        lst =[[nums[0],0]]
        for i in range(1,len(nums)):
            cnt =0 
            while lst and lst[-1][0]< nums[i]:
                cnt =max( cnt +1,lst[-1][1])
                lst.pop()
            lst.append([nums[i],cnt])
            ans = max(ans,cnt)
            #print(lst)
        return ans
                 
re= Solution().totalSteps([1682,63,124,147,897,1210,1585,1744,1764,1945,323,984,1886,346,481,1059,1388,1483,1516,1842,1868,1877,504,1197,785,955,970,1848,1851,398,907,995,1167,1214,1423,1452,1464,1474,1311,1427,1757,1992,57,1625,1260,700,725])    
#re= Solution().totalSteps([10,6,5,10,15])
re = Solution().totalSteps([7,14,4,14,13,2,6,13])
print(re)            