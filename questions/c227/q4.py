from bisect import bisect_right
class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        ls1 = nums[:n//2]
        ls2 = nums[n//2:]
        def getComb(ls,res):
            for i in ls:
                re =[]
                for t in res:
                    re.append(t+i)
                res = res +re
            return res
        cob1 = getComb(ls1,[0])
        cob2 = getComb(ls2,[0])
        cob1.sort()
        cob2.sort()
        mx = abs(goal)
        m= len(cob2)
        #print(cob1,cob2)
        for i in cob1:
            t = goal - i
            idx = bisect_right(cob2,t)
            print(t,idx)
            if idx >0:
                mx = min(mx, abs(cob2[idx-1]-t))
            if idx < m:
                mx = min(mx, abs(cob2[idx]-t))
            if idx ==0:
                mx = min(mx, abs(cob2[0]-t))
        return mx

re =Solution().minAbsDifference(nums = [1,2,3], goal = -7)
print(re)