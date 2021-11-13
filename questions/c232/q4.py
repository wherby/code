class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q =[(0,-1)]
        mx =0
        nums.append(0)
        for i,a in enumerate(nums):
            if a >= q[-1][0]:
                q.append((a,i))
            else:
                while a < q[-1][0]:
                    b,idx= q.pop()
                    t = b* (i-idx)
                    if idx <=k and i-1 >=k:
                        mx = max(mx,t)
                q.append((a,idx))
            #print(q)
        return mx

re = Solution().maximumScore(nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872], k = 5)
print(re)