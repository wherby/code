#https://leetcode-cn.com/problems/minimum-incompatibility/
import collections
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        c = collections.Counter(nums)
        
        for _,v in c.items():
            if v > k:
                return -1
        n = len(nums)
        keys =list(c.keys())
        keys.sort()
        ans = 10**9
        def backtrack(idx,cur_num,cur_list,delta):
            nonlocal ans
            if delta > ans: return
            if len(cur_list)  == n//k:
                delta +=cur_list[-1] - cur_list[0]
                cur_list = []
                cur_num =-1
            if idx ==n:
                ans = min(ans,delta)
                return
            for i in keys:
                if i <= cur_num or c[i] ==0: continue
                c[i] -=1
                cur_list.append(i)
                backtrack(idx +1,i,cur_list,delta)
                cur_list.pop()
                c[i] +=1
                if len(cur_list) ==0:
                    break
        backtrack(0,-1,[],0)
        return ans

re = Solution().minimumIncompatibility([6,3,8,1,3,1,2,2],4)
print(re)