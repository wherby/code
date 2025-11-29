# https://codeforces.com/gym/106197/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1126/solution/cf106197g.md
# 几个技巧：
# 建立 next_pos[value][idx] 表示从index 开始，下一个value 出现的位置
# later_longest_full[idx] 维护了从idx开始，可以完成多少次 数字完整覆盖，就是可以自由组合多少位
# 最后用  while pos <= n: 试填法，找到当前位置最大的满填数字


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        s = [int(c) for c in I()]
        
        if 0 not in s: outs.append('0')
        else:
            n = len(s)
    
            next_pos = [[n] * (n + 1) for _ in range(10)]
            
            for i in range(n - 1, -1, -1):
                for j in range(10):
                    next_pos[j][i] = next_pos[j][i + 1]
                next_pos[s[i]][i] = i
    
            later_longest_full = [0] * (n + 1)
            later_longest_full[n] = -1
            
            cnt = [0] * 10
            cur = 0
            res = 0
            
            for i in range(n - 1, -1, -1):
                later_longest_full[i] = res
    
                if cnt[s[i]] == 0:
                    cnt[s[i]] = 1
                    cur += 1
                
                if cur == 10:
                    cur = 0
                    res += 1
                    for j in range(10):
                        cnt[j] = 0
    
            ans = []
            pos = 0
            
            while pos <= n:
                mi = n + 5
                choice = -1
    
                for i in range(0 if ans else 1, 10):
                    if later_longest_full[next_pos[i][pos]] < mi:
                        mi = later_longest_full[next_pos[i][pos]]
                        choice = i
                
                ans.append(choice)
                pos = next_pos[choice][pos] + 1
            
            outs.append(''.join(map(str, ans)))
    
    print('\n'.join(outs))

main()