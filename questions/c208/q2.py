class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        remain=0
        mx =0
        cnt =0
        sm =0
        n = len(customers)
        idx =0
        while idx<n or remain >0:
            #print(remain,sm,cnt)
            if idx <n:
                remain = remain + customers[idx] 
            cn =0
            if remain >=4:
                remain =remain -4
                cn = 4
            else:
                cn = remain
                remain = 0
            g = cn*boardingCost -runningCost
            sm +=g
            if sm >mx:
                mx = sm
                cnt =idx+1 
            idx +=1
        
        return cnt if cnt>0 else -1

re = Solution().minOperationsMaxProfit(customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92)
print(re)