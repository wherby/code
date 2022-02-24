# bruteForceForStateCompression 状态合并
https://leetcode-cn.com/problems/distribute-repeating-integers/submissions/

把不同的数字作为阶段，不同的分配作为状态，进行状态转移。

给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：

第 i 位顾客 恰好 有 quantity[i] 个整数。
第 i 位顾客拿到的整数都是 相同的 。
每位顾客都满足上述两个要求。
如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。

 

示例 1：

输入：nums = [1,2,3,4], quantity = [2]
输出：false
解释：第 0 位顾客没办法得到两个相同的整数。
示例 2：

输入：nums = [1,2,3,3], quantity = [2]
输出：true
解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
示例 3：

输入：nums = [1,1,2,2], quantity = [2,2]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
示例 4：

输入：nums = [1,1,2,3], quantity = [2,2]
输出：false
解释：尽管第 0 位顾客可以得到 [1,1] ，第 1 位顾客没法得到 2 个一样的整数。
示例 5：

输入：nums = [1,1,1,1,1], quantity = [2,3]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [1,1,1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-repeating-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```
from collections import Counter 
class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """ 
        nc = Counter(nums)
        ls =list(nc.values())
        #print(ls)
        n = len(ls)
        dp = [[False]*1024 for _ in range(51)]
        for i in range(n+1):
            dp[i][0] = True
        m = len(quantity)
        dic = {}
        for i in range(2**m):
            cnt =0
            for j in range(m):
                if (1<<j) & i :
                    cnt += quantity[j]
            dic[i] = cnt
        #print(dic,ls)
        for i in range(1,n+1):
            for state in range(1,2**m):
                if dp[i-1][state] == True:
                    dp[i][state] = True
                    continue
                subset = state
                while subset>0:
                    if dp[i-1][state-subset] == False:
                        subset = (subset)-1 &state
                        continue
                    #print(ls[i-1],dic[subset],subset)
                    if ls[i-1] >= dic[subset]:
                        dp[i][state] = True
                        break
                    subset = (subset)-1 &state
        return dp[n][(2**m)-1]
```
状态转移用dfs，用deepcopy记录状态
```
from functools import lru_cache 
from collections import Counter 
class Solution(object):
    def canDistribute(self, nums, quantity):
        m = len(quantity)
        quantity.sort()

        @lru_cache
        def dp(con,i):
            if i ==-1:
                return True
            
            if quantity[i] > con[0]:
                return False
            
            for j in range(len(con)):
                if con[j] >= quantity[i]:
                    new_con = list(con)
                    new_con[j] -= quantity[i]
                    new_con.sort(reverse=True)

                    if dp(tuple(new_con),i-1):
                        return True
                else:
                    break
            return False
        return dp(tuple(t for _, t in Counter(nums).most_common(m)),m-1)
```