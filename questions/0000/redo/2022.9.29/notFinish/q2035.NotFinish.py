# https://leetcode.com/contest/weekly-contest-262/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
    


class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 10**10
        n = len(nums)
        half = n //2
        def verify(state):
            nonlocal mx
            acc1,acc2 =0,0
            for i in range(n):
                if (1<<i) & state:
                    acc1 += nums[i]
                else:
                    acc2 += nums[i]
            mx =min(mx, abs(acc1-acc2))
            
        def allState(k,m=8):
            state = (1<<k) -1
            while (state <(1<<m)):
                verify(state)
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
        allState(half,n)
        return mx
ls=[7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]
re = Solution().minimumDifference(ls)
print(re)
        