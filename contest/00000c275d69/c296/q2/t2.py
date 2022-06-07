class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt =0
        tmp =[]
        nums.sort()
        mx,mn = nums[0],nums[0]
        for a in nums:
            mx = max(mx,a)
            mn = min(mn,a )
            if mx -mn >k:
                cnt +=1
                #print(tmp,a)
                tmp =[]
            if len(tmp) ==0:
                mx,mn = a ,a
            tmp.append(a)
        if len(tmp) >0:
            cnt +=1
        return cnt
        
        
re =Solution().partitionArray(nums = [3,6,1,2,5], k = 2)
print(re)