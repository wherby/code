class Solution:
    def sumOfBeauties(self, nums):
        n =len(nums)
        isT1 = True
        re =[0]*n
        mi = [0]*(n+2)
        ma = [10**8]*(n+2)
        for i in range(n):
            mi[i+1] =max(mi[i+1],nums[i],mi[i])
            ma[n-i] = min(ma[n-i],nums[n-i-1],ma[n-i+1])
        print(mi,ma)
        cnt =0
        for i in range(1,n-1):
            if nums[i] >mi[i] and ma[i+2] >nums[i]:
                cnt +=2
            elif nums[i] >nums[i-1] and nums[i+1] >nums[i]:
                cnt +=1
            
        return cnt

re=Solution().sumOfBeauties([1,2,3])
print(re)