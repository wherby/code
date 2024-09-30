
# Question

https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i

## 

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(idx,rem):
            if idx == n :
                return 0
            ret = 0 
            for j in range(idx+1,n):
                if nums[idx]== nums[j]:
                    ret = max(ret, 1+dfs(j,rem))
                elif rem >0:
                    ret = max(ret,1+dfs(j,rem-1))
            return ret
        ret = 0
        for i in range(n):
            ret = max(ret,dfs(i,k) +1)
        return ret

DP 优化
维护 （a,i) 表示以a结尾，用了i次的最大值，并且有一个mx数组维护 i次使用的最大值，提供转移方程的时候压缩其他值

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mx = [0]*(k+1) 
        dic = defaultdict(int)
        ret =0
        for a in nums:
            for i in range(k,-1,-1):
               dic[(a,i)] = max(dic[(a,i)] + 1, mx[i-1]+1 if i >0 else 0)
               ret= max(ret, dic[(a,i)])
               mx[i] = max(mx[i],dic[(a,i)])
               #print(a,mx,ret,dic)
        return ret 
