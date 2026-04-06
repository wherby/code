# https://codeforces.com/gym/106443/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0330/solution/cf106443d.md
# 如果没有平局的情况下，如果从一个状态能到达的所有状态都是必胜的，则这个状态必负，否则必胜。
# 要计算它所能到达的状态是否必胜，则查询它能达到的是否都是必胜，而状态转移的时候，是连续的区间，到达的区间是连续的，所以可以用前缀和记录是否都必胜



import init_setting
from cflibs import *
def main(): 
    M = 5 * 10 ** 5 + 5
    dp = [0] * M
    dp_acc = [0] * (M + 1)
    
    for i in range(1, M):
        if dp_acc[i] - dp_acc[i // 2] != i - i // 2:
            dp[i] = 1
        dp_acc[i + 1] = dp_acc[i] + dp[i]
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        outs.append('mastermei' if dp[n] else 'the greatest')
    
    print('\n'.join(outs))
    print(dp[:10])

if __name__ == '__main__':
    main()
