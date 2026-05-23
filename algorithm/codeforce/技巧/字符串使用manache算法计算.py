# https://codeforces.com/gym/105745/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0414/solution/cf105745f.md
# 使用manache 计算标记前缀能删到哪里的位置
# 这时要计算所有前后缀删除的时候[l,r] 所有的种类
# 使用的统计算法很巧妙，cur计算前缀和，如果下一个字符不是后缀的断点的话，则不统计，这些前缀和在后面的后缀的断点处累加到结果
# 这样就计算了 所有可能的 L,R 组合



import init_setting
from cflibs import *
def main(): 
    def possible_positions(s):
        tmp = '*'.join(s)
        manacher = [0] * (2 * n - 1)
        idx = 0
        
        for i in range(1, 2 * n - 1):
            if idx + manacher[idx] >= i:
                manacher[i] = fmin(idx + manacher[idx] - i, manacher[2 * idx - i])
            while i - manacher[i] - 1 >= 0 and i + manacher[i] + 1 < 2 * n - 1 and tmp[i - manacher[i] - 1] == tmp[i + manacher[i] + 1]:
                manacher[i] += 1
            if i + manacher[i] > idx + manacher[idx]:
                idx = i
        
        ans = [0] * (n + 1)
        ans[0] = 1
        to_fill = 0
        
        for i in range(1, 2 * n - 1, 2):
            if i > to_fill and i - manacher[i] <= to_fill:
                ans[(2 * i - to_fill) // 2 + 1] = 1
                to_fill = 2 * i - to_fill + 2
        
        return ans
    
    s = I()
    n = len(s)
    
    pre = possible_positions(s)
    suf = possible_positions(s[::-1])
    suf.reverse()
    
    ans = 0
    cur = 0
    
    for i in range(n):
        cur += pre[i]
        ans += cur * suf[i + 1]
    
    print(ans)