# https://codeforces.com/gym/105845/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1217/solution/cf105845f.md
# dp[n][j] 表示n个数分j段， 在这个顺序里，比较难处理状态转移的问题
# 如果dp[j][n] 从分的次数开始递推则可以利用同余特性得到状态转移

# 假设有 n 名学生排成一列，每人有一个整数值。你的任务是将这一列学生分成一个或多个连续的小组（小组个数 m 不固定），
# 使得每个小组都满足一个特殊的“凸包”条件：第一个小组从第 1 名学生开始，最后一个小组以第 n 名学生结束。
# 小组是连续的；如果第 j 个小组覆盖了从下标 lj​  到 rj 的学生，则对于每个 1≤j<m，有 rj+1=lj+1。对于每个小组 j（其中 1≤j≤m），
# 如果该小组包含下标为 lj,lj+1,…,rj 的学生，那么和 lj+lj+1+⋯+rj​  必须能被 j 整除。你的任务：计算形成这种学生划分的方式数，并将答案对 109+7取模后输出

# cur 记录当前j index 下同余的数量， ndp记录的是合法转移，在下一index开始前，当前j的上一轮结束的同余数量可以被后面使用
# ndp 记录的是在i轮情况下，以当前元素结尾的符合同余的个数,dp记录的是前一轮的完结数，

import init_setting
from cflibs import *
def main(): 
    n = II()
    mod = 10 ** 9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    ans = 0
    
    for i in range(1, n + 1):
        ndp = [0] * (n + 1)
        
        cur = [0] * i
        pre = 0
        
        for j in range(n + 1):
            pre = (pre + j) % i
            ndp[j] = cur[pre]
            cur[pre] = (cur[pre] + dp[j]) % mod
        
        dp = ndp
        ans = (ans + dp[n]) % mod
    
    print(ans)

main()