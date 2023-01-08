# https://leetcode.cn/contest/weekly-contest-321/problems/count-subarrays-with-median-k/
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pre = [0]*(n+1)
        acc =0 
        idx = nums.index(k)
        for i,a in enumerate(nums):
            if a >k:
                pre[i+1] = pre[i]+1
            elif a <k:
                pre[i+1] = pre[i] -1
            else:
                pre[i+1] = pre[i]
        dic = [0]*(n*2)
        for i in range(idx+1):
            dic[pre[i]+ n] +=1
        cnt =0 
        print(dic,pre)
        for i in range(idx+1,n +1):
            cnt  += dic[pre[i]+n] + dic[pre[i]+n-1]
            #print(cnt)
        return cnt

re =Solution().countSubarrays([3,2,1,4,5],4)
print(re)