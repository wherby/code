#subset without dup https://leetcode.com/submissions/detail/532680686/?from=explore&item_id=3837
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = [[]]
        
        start = 0
        
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                start = size
            else:
                start = 0
            
            size = len(ans)
            for j in range(start, len(ans)):
                ans.append(ans[j] + [nums[i]])
        
        return ans
