# https://codeforces.com/gym/106732/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1002/solution/cf106732c.md
# 如果是求最大值的时候，D类读者只有前面的分比自己期望的分少，才能增加分数，所以需要贪心让比自己期望分少的读者先被处理。所以用期望值排序
# 如果是求最小值的时候。这时用对称性从大到小处理就好了
# 这里为了复用solve， 做了镜面反转




import init_setting
from cflibs import *
def main():
    n, m = MII()
    
    types = []
    score = []
    
    for _ in range(m):
        t, x = LI()
        types.append(1 if t == 'S' else 0)
        score.append(int(x))
    
    def solve():
        cnt = 0
        cur = 0
        for i in sorted(range(m), key=lambda x: score[x]):
            cnt += 1
            if types[i]: cur += score[i]
            else: cur = fmin(cur + n, fmax(cur + 1, score[i] * cnt))
        return cur / cnt
    
    mx = solve()
    
    for i in range(m):
        score[i] = n + 1 - score[i]
    
    mn = n + 1 - solve()
    
    print(f'{mn:.15f} {mx:.15f}')