# TDK 暴力搜索 Timeout
from collections import defaultdict
import collections
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = collections.Counter(nums)
        
        for _,v in c.items():
            if v > k:
                return -1
        mn = 10**9
        n= len(nums)
        nums.sort()
        visited =[0]*n
        visited[0] =1
        def dfs(cur,count,low,high,sm): #排序之後用low,和high 記錄最大最小值
            nonlocal mn
            #print(cur,count,low,high,sm)
            if sm > mn:  # 如果不加這個優化，python會timeout
                return
            if count == n:
                    #print(visited)
                    #print(sm,high,low,mn)
                    mn = min(mn, sm +high-low)
            if count%(n//k) == 0:
                #print(count)
                for i in range(n):
                    if visited[i] ==0:
                        visited[i] =1
                        #print(visited,i,k,count)
                        dfs(i,count +1,nums[i],nums[i],sm + high-low)
                        visited[i] =0
                        break
            else:
                for i in range(cur,n):
                    if visited[i] !=0: continue
                    if nums[i] == high: continue  #根據題意 一個組合裏不能有兩個相同值
                    visited[i] =1
                    dfs(i+1,count+1,low,nums[i],sm)
                    visited[i]=0
        dfs(1,1,nums[0],nums[0],0)
        #print(mn)
        return mn
            




re = Solution().minimumIncompatibility([6,3,8,1,3,1,2,2],4)
print(re)
