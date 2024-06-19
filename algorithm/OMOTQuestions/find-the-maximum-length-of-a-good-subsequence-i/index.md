
# Question
https://leetcode.cn/contest/biweekly-contest-132/problems/find-the-maximum-length-of-a-good-subsequence-i/description/

给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。

请你返回 nums 中 好 
子序列
 的最长长度

 

示例 1：

输入：nums = [1,2,1,1,3], k = 2

输出：4

解释：

最长好子序列为 [1,2,1,1,3] 。

示例 2：

输入：nums = [1,2,3,4,5,1], k = 0

输出：2

解释：

最长好子序列为 [1,2,3,4,5,1] 。

如果用dfs定义状态，则爆内存
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        
        @cache
        def dfs(lstv,idx,cnt):
            if cnt ==0:
                return len(dic[lstv]) - bisect_left(dic[lstv], idx)
            if idx ==n:
                return 0
            if nums[idx] == lstv:
                return dfs(lstv,idx+1,cnt)+1
            return max(dfs(nums[idx],idx+1,cnt-1)+1,dfs(lstv,idx+1,cnt))
        return dfs(-1,0,k+1)
        
re =Solution().maximumLength([30,30],0)
print(re)

用状态压缩的概念，把状态压缩成上一个是相同和不同的时候  contest\00000c397d130\d132\q4


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(int)
        mx = 0
        dick = defaultdict(int)
        for a in nums:
            for j in range(k,-1,-1):
                dic[(a,j)] = max(dic[(a,j)]+1,dick[j-1]+1 )
                dick[j] = max(dick[j], dic[(a,j)])
                mx = max(mx,dic[(a,j)])
        #print(dic,dick)
        return mx 