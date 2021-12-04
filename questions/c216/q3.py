class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        ls = [0]*(n+2)
        lsr = [0]*(n+2)
        for i in range(n):
            ls[i+2] =ls[i] + nums[i]
            lsr[n-1-i] = lsr[n+1-i] + nums[n-1-i]
        #print(ls,lsr)

        cnt = 0 
        for i in range(n):
            if ls[i+1] + lsr[i+2] == ls[i]+lsr[i+1]:
                cnt +=1
        #print(cnt)
        return cnt

            


        
re =Solution().waysToMakeFair(nums = [1,1,1])