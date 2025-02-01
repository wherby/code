## Algorithms for Competitive Programming- [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html#generic-implementation)
contest/acf/test/q1/q1.py


## DP 方向问题
如果知道边界情况的时候，就能确定dp的方向

比如扔鸡蛋，【# dfs(i,j) 表示用i次扔和j个鸡蛋能测试多少层楼】 这里只有每次一次之后 不同情况的i,j减少，同时 
```python
if i ==0 or j ==0:
    return 0 
```
的边界情况
algorithm/dp/扔鸡蛋/s1.py

如果是计算第2类斯特林数的情况，把N个人分成M组 [# (i,j)表示第i个人的时候，由(i-1,j-1)情况再加一个新组和(i-1,j)情况加入已有的j组两个情况转化而来]，这时候只能从(i,j)是由什么状态转化而来递推更方便
```
for i in range(1,MX):
    for j in range(1,MX):
        s[i][j] = (s[i-1][j-1] + j * s[i-1][j]) % mod 
```
algorithm/mathA/第2类斯特林数/find-the-number-of-possible-ways-for-an-event.py

## 2D dp 物品可以直接先放入DP 再计算
https://leetcode.cn/contest/weekly-contest-298/problems/selling-pieces-of-wood/

class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """ 
        dp = [[0]*(n+1) for _ in range(m+1)]
        for y,x,p in prices:
            dp[y][x] = p
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]= max(dp[i][j], dp[i-1][j])
                dp[i][j]= max(dp[i][j], dp[i][j-1])
        for i in range(1,m+1):
            for j in range(1,n+1):
                for k in range(1,i):
                    dp[i][j] = max(dp[i][j],dp[k][j]+dp[i-k][j])
                for k in range(1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k] + dp[i][j-k])
        return dp[m][n]

## 覆盖问题
algorithm\dp\覆盖问题\cover.py
https://leetcode.cn/contest/biweekly-contest-74/problems/minimum-white-tiles-after-covering-with-carpets/
class Solution:
    def minimumWhiteTiles(self, floor: str, num: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0]*(num+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] += dp[i-1][0] +(floor[i] =="1")
            if i+1 >=carpetLen:
                for j in range(1,num+1):
                    dp[i][j] = min(dp[i-1][j] + (floor[i] =="1"),dp[i-carpetLen][j-1])
       # print(dp)
        return min(dp[n-1])



## DP 技巧

把DP所有情况计算完成，然后去掉不合法的情况

https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/D?source=facebook
contest/meta2024/r1/q4/substitution_cipher__slime_source_code.cpp


https://leetcode.cn/problems/count-the-number-of-inversions/solutions/2953751/python3javacgotypescript-yi-ti-yi-jie-do-73li/?envType=daily-question&envId=2024-10-17
algorithm/dp/反向dp/count-the-number-of-inversions/index.py


## DP 单调转移 <-前后状态单调性
状态具有单调性
algorithm/dp/dp保留选择排序
dp[i+1][j] = min(dp[i][j],(s1-c,sorted(ids + [idx])))

## 值域DP,利用单调性累积  <-属性单调性，按照属性单调性的方向求值累积
algorithm/dp/值域DP/longest-subsequence-with-decreasing-adjacent-difference
用数组代替dictionary 可以提高速度  https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/submissions/

## 选择连续区域，状态机dp

https://leetcode.cn/problems/maximum-frequency-after-subarray-operation/solutions/3057702/mei-ju-zhuang-tai-ji-dp-by-endlesscheng-qpt0/