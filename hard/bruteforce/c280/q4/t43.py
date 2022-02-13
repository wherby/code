# bruteforce
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        def doSomething(state,a):
            for i in range(2* numSlots):
                if state & (1<<i):
                    dp2[state] = max(dp2[state],dp[state-(1<<i)] + (a & (i//2 +1)) )

        def allState(k,a):
            m=numSlots*2
            state = (1<<k) -1
            while (state <(1<<m)):
                doSomething(state,a)
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
                #print("New State: ", bin(state))
        state = 2**(2*numSlots)
        dp = [0]*state
        dp2= [0]*state
        n = len(nums)
        for i,a in enumerate(nums):
            allState(i+1,a)
            dp = dp2
            #print(dp[:10])
        return max(dp)

re = Solution().maximumANDSum(nums = [10,10,1,3,6,13,2], numSlots = 8)
print(re)
re = Solution().maximumANDSum(nums = [4,2,2,11,7,12,9,8], numSlots = 4)
print(re)

re = Solution().maximumANDSum(nums = [8,13,3,15,3,15,2,15,5,7,6], numSlots = 8) # timeout
print(re)