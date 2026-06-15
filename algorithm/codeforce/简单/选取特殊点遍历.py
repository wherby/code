# https://codeforces.com/gym/104755/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0610/solution/cf104755f.md
# 假设每个点都是最边沿的点，然后用特殊点得到光源的可能点来判定



import init_setting
from lib.cflibs import *
def main():
    n, m = MII()
    holes = LII()
    targets = LII()
    
    rnd = random.getrandbits(20)
    d = {v ^ rnd: i for i, v in enumerate(targets)}
    
    mi = min(holes)
    
    ans = []
    vis = [0] * m
    
    for v in targets:
        flg = True
        
        for x in holes:
            if (v + 2 * (x - mi)) ^ rnd not in d:
                flg = False
        
        if flg:
            ans.append(2 * mi - v)
            for x in holes:
                vis[d[(v + 2 * (x - mi)) ^ rnd]] = 1
    
    if min(vis):
        print('Yes')
        print(len(ans))
        print(*ans)
    else:
        print('No')