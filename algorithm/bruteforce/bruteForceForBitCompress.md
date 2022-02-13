# 状态压缩，字节位压缩
 https://leetcode-cn.com/contest/weekly-contest-280/problems/maximum-and-sum-of-array/

给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为 1 到 numSlots 。

你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。

比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。
请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。


numSlots其实是2*numSlots个bit状态
这里在每个篮子里的bit位是等价的，所以相邻的两个字节压缩为（0，1，2）3个状态
```
    for j in range(numSlots):
        c  =(state >>(2*j)) &3
        if c <2:
            state2  = (state & ~(3<<(2*j))) |((c+1)<<(2*j))
```


# dp bruteforce 在解决背包问题的时候可能需要两个dp数组

```
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        def doSomething(state,a):
            for i in range(2* numSlots):
                if state & (1<<i):
                    dp2[state] = max(dp2[state],dp[state-(1<<i)] + (a & (i//2 +1)) )

        def allState(k,a):
            m=numSlots*2
            state = (1<<k) -1
            while (state <(1<<m)):
                doSomething(state,a)
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
                #print("New State: ", bin(state))
        state = 2**(2*numSlots)
        dp = [0]*state
        dp2= [0]*state
        n = len(nums)
        for i,a in enumerate(nums):
            allState(i+1,a)
            dp = dp2
            #print(dp[:10])
        return max(dp)
```