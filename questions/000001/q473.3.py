from collections import Counter 
import functools
class Solution:
    def makesquare(self, mats) -> bool:
        n = len(mats)
        mats.sort(reverse =True)
        if sum(mats)%4 != 0:
            return False
        k = sum(mats) //4
        fd =False
        #print(k)
        @functools.lru_cache(None)
        def dfs(turn,acc, idx,status):
            nonlocal fd
            #print(turn,acc,idx,bin(status))
            last =-1
            if acc == k:
                acc =0
                turn +=1
                idx =0
            if turn ==4:
                fd =True
                return 
            if idx ==n:
                return
            for i in range(idx,n):
                if status &(1<<i) ==0 and acc + mats[i] <= k and last != mats[i]:
                    status = status + (1<<i) 
                    last = mats[i]
                    dfs(turn,acc + mats[i],idx +1,status)
                    status = status - (1<<i) 
            
        dfs(0,0,0,0)
        return fd

#re = Solution().makesquare([1,1,2,2,2])
#re = Solution().makesquare([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
#re = Solution().makesquare([2,2,2,2,2,6])
re = Solution().makesquare([13,11,1,8,6,7,8,8,6,7,8,9,8])
print(re)
                    