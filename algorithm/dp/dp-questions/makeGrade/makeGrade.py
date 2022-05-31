## 已知数组A 构造单调数组B使得两个数组的距离和最小 
# algorithm\dp\dp-questions\makeGrade\pic\makeGrade.png
from math import inf

def work(ls):
    b = list(ls)
    b.sort()
    n = len(b)
    dp = [[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(n):
        mn = inf 
        for j in range(n):
            mn = min(mn, dp[i][j+1])
            dp[i+1][j+1] = mn + abs(ls[i] -b[j])
    return dp[n][n]

def makeGrade(ls):
    mn = work(ls)
    ls = ls[::-1]
    mn = min(mn, work(ls))
    return mn

a =[1,3,2,4,5,3,9]
print(makeGrade(a))