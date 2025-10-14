# https://codeforces.com/gym/103855/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1013/solution/cf103855m.md
# 绝对值对的最小值，利用等式转换 algorithm/mathA/abs/index.md






import init_setting
from cflibs import *
def main():
    n = II()
    p = LII()
    q = LII()
    
    def calc(xs):
        mi = min(xs)
        ma = max(xs)
        
        cnt = [0] * (ma - mi + 1)
        for x in xs:
            cnt[x - mi] += 1
        
        vals = []
        for i in range(ma - mi + 1):
            for _ in range(cnt[i]):
                vals.append(mi + i)
        
        return sum((2 * i - (n - 1)) * vals[i] for i in range(n))
    
    v1 = calc(p)
    v2 = calc(q)
    
    v3 = calc([p[i] - q[i] for i in range(n)])
    v4 = calc([p[i] + q[i] for i in range(n)])
    
    print((v1 + v2) * 2 - v3 - v4)