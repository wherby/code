

## 
contest\00000c275d69\c313\q4
https://leetcode.cn/contest/weekly-contest-313/problems/maximum-deletions-on-a-string/
dp 状态选择： contest\00000c275d69\c313\q4\t4.3.py
递归：contest\00000c275d69\c313\q4\t4.2.py

## 搭桥过河 DP + 单调栈
https://leetcode.cn/problems/NfY1m5/solution/by-yingying_-hd6g/

https://www.cnblogs.com/wyzwyz/p/14038855.html


## 合并状态：
https://leetcode.cn/problems/domino-and-tromino-tiling/
algorithm/dp/questions/domino-and-tromino-tiling.py
dp[i][3] = dp[i][0] + dp[i-1][0] + dp[i-1][1] + dp[i-1][2]  ###  dp[i-1][0] 是两个横放的状态，如果不合并就会有更多的状态
