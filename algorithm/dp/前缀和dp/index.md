

## 前缀和DP
给你一个整数数组 nums 和一个整数 k。你的任务是将 nums 分割成一个或多个 非空 的连续子段，使得每个子段的 最大值 与 最小值 之间的差值 不超过 k。
https://leetcode.cn/problems/count-partitions-with-max-min-difference-at-most-k

这里需要知道所有DP[i]构成的前缀和，才能达到在求下个个DP的时候，dp[i] = pre[i-1] - pre[left] 的操作
而在双指针的时候，left是0开始的，而dp[0] = pre[i-1]- pre[0], 要让i-1有意义，对应pre数组需要平移2位
dp[i] = pre[i+1]- pre[left]
pre[i+2] = pre[i+1]+ dp[i]

pre[0] = 0 
pre[1] = 1 
pre[2] = pre[1] + dp[0]
pre[i+2] = pre[i+1] + dp[i] 