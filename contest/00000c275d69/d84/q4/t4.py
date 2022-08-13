class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mx = nums[n-1]
        acc = 0
        for i in range(n-1,-1,-1):
            t = nums[i]
            if t <=mx:
                mx = t 
            else:
                acc += t //mx 
                if t%mx !=0:
                    mx = (t //(t//mx+1))
                else:
                    acc -=1
        return acc




re =Solution().minimumReplacement([2,7,3])
print(re)