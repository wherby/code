
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
        cob2.sort(reverse=True)
        mn = abs(goal)
        l,r =0,0
        n1,n2 = len(cob1),len(cob2)
        while l <n1 and r <n2:
            ts = cob1[l] + cob2[r]
            mn =min(mn,abs(goal-ts))
            if mn ==0:
                return 0
            if ts <goal:
                l +=1
            else:
                r +=1
        return mn

re =Solution().minAbsDifference(nums = [5,-7,3,5], goal = 6)
print(re)