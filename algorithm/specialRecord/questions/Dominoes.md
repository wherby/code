

# https://codeforces.com/problemset/problem/342/D
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/03/0314/solution/cf342d.md

3级多米诺排列 ？？

···

def fc(must):
    dp= [0]*8
    ndp =[0]*8 
    dp[0]= 1
    print(dp)
    for v0 in range(8):
        for v1 in range(8):
            if v1 & must == 0 and v0 & v1 == 0 and v0 & must == 0 and (7 - v1 - must - v0) % 3 == 0:
                ndp[v1] += dp[v0]
                print(must, v0, " -> ", v1,ndp)
    print(ndp)


for i in range(8):
    fc(i)
#fc(0)
···