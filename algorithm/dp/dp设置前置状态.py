# https://codeforces.com/gym/102791/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0913/solution/cf102791j.md
# 这里字符串分割的时候，需要当前点和分割点一样，而且分割的前一个点也是合适的分割点，并且取得分割的前缀最优
# 怎么维持分割点的前一个分割点也是合格的分割点 的判定
#
# 用 dp[i - 1] > saved_ans[s[i - 1]]: 来判定，设置dp[0] = 0 表示 0长度是一个分割的端点，任何dp[i-1]!= -inf 情况下，都认为 i-1是一个合格的分割点
# 
# saved_ans[s[i]] 表示用 s[i]作为起始分割点，可以获得的最大分段数目
# saved_pos[s[i]] 表示  s[i]作为分段的时候，取得最大数目的时候，分割pos 位置

# 在循环的时候，看i 的前一个点是否为可以被分割的最大分段的点，如果是，则更新s[i-1]相关的值
#             对于当前点，通过已经记录s[i]分割的点的记录，转移到下一个值
#             看似只分析了 i-1,i， dp[i - 1] > saved_ans[s[i - 1]] 这里已经保证了分割的成立

import init_setting
from codeforce.lib.cflibs import *
def main():
    n = II()
    s = [ord(c) - ord('a') for c in I()]
    
    inf = 10 ** 6
    
    saved_ans = [-inf] * 26
    saved_pos = [-1] * 26
    
    dp = [-inf] * (n + 1)
    pre = [-1] * (n + 1)
    
    dp[0] = 0
    
    for i in range(1, n):
        if dp[i - 1] > saved_ans[s[i - 1]]:
            saved_ans[s[i - 1]] = dp[i - 1]
            saved_pos[s[i - 1]] = i - 1
        
        if saved_ans[s[i]] >= 0:
            dp[i + 1] = saved_ans[s[i]] + 1
            pre[i + 1] = saved_pos[s[i]]
    
    if dp[n] < 0: print(-1)
    else:
        print(dp[n])
        
        tmp = []
        cur = n
        
        while cur:
            tmp.append(cur - pre[cur])
            cur = pre[cur]
        
        tmp.reverse()
        
        print(' '.join(map(str, tmp)))

main()