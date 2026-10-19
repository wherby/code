# https://leetcode.cn/problems/maximum-alternating-subarray-sum-with-one-deletion/description/
# 子数组多状态： 长度奇偶性，与是否减去1的状态
# 使用状态转移

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        inf=-10**18
        e0=e1=o0=o1=inf
        ans=inf
        for x in nums:
            ne0=ne1=no0=no1=inf
            
            no0=max(no0,e0+x)
            ne0=max(ne0,o0-x)
            no1=max(no1,e1+x)
            ne1=max(ne1,o1-x)
            
            ne1=max(ne1,e0)
            no1=max(no1,o0)

            no0=max(no0,x)

            e0,o0,e1,o1=ne0,no0,ne1,no1

            ans=max(ans,e0,e1,o0,o1)
        return ans