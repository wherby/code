from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = [[-1] for _ in range(32) ]
        for i,a in enumerate(nums):
            for j in range(32):
                if (1<<j)&a:
                    ls[j].append(i)
        n = len(nums)
        ret =[1]*len(nums)
        idx = [0]*32
        for i in range(n):
            mx = 1
            for j in range(32):
                if idx[j]< len(ls[j]) and ls[j][idx[j]]<i:
                    idx[j] +=1
                if idx[j] < len(ls[j]) and ls[j][idx[j]]>=i:
                    mx = max(mx, ls[j][idx[j]] -i +1)
            ret[i] = mx 
        return ret

re =Solution().smallestSubarrays(nums = [1,2])
print(re)