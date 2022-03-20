import heapq
class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm = sum(nums)
        hf = sm*1.0 /2 *-1
        st = []
        for a in nums:
            heapq.heappush(st,-a)
        ret,cnt =0,0
        while ret > hf:
            a = heapq.heappop(st)
            cnt +=1
            ret += a *1.0/2
            heapq.heappush(st,a /2)
        return cnt

re = Solution().halveArray([1])
print(re)
