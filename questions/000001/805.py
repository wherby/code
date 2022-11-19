from typing import List, Tuple, Optional
from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n= len(nums)
        avag = sum(nums) / n 
        
        ls1,ls2 = nums[:n//2],nums[n//2:]
        m = len(ls2)
        dic =defaultdict(list)
        def dfs(idx,acc,cnt):
            if idx ==m:
                dic[cnt].append(acc)
                return
            dfs(idx+1,acc + ls2[idx],cnt +1)
            dfs(idx+1,acc,cnt)
        dfs(0,0,0)
        m2 = len(ls1)
        fd = False
        for i in range(m+1):
            ls = dic[i]
            dic[i] = sorted(ls)
        def ifFind(acc,cnt):
            for i in range(m+1):
                if i + cnt ==0 or i+cnt ==n:continue
                res = (cnt+i)*avag - acc 
                
                k= bisect_left(dic[i],res-0.01)
               # print(res,dic[i][k],dic[i],acc,cnt)
                if k < len(dic[i]) and abs(dic[i][k]-res)<=0.001:
                    return True
            return False
        def dfs2(idx,acc,cnt):
            nonlocal fd
            #print(idx,acc,cnt)
            if idx ==m2:
                if ifFind(acc,cnt):
                    fd =True
                return
            dfs2(idx+1,acc + ls1[idx],cnt +1)
            dfs2(idx+1,acc,cnt)
        dfs2(0,0,0)
        return fd
        
re =Solution().splitArraySameAverage(nums = [3,1])
print(re)