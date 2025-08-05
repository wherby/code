from typing import List, Tuple, Optional

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        acc = 0 
        for a in nums:
            acc |= a 
        sm =acc 
        n = len(nums)
        cnt = 0
        def dfs(idx,acc):
            nonlocal cnt
            if idx == n:
                if acc ==sm:
                    cnt +=1
                return 
            if acc> sm:
                return
            dfs(idx+1,acc|nums[idx])
            dfs(idx+1,acc)
        dfs(0,0)
        return cnt

re = Solution().countMaxOrSubsets(nums = [3,2,1,5])
print(re)