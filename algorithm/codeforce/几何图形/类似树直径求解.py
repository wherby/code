# https://codeforces.com/gym/106124/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0209/solution/cf106124d.md
# 此题求解类似求解树直径的思路，先从任意点出发找到最远的点，再从这个点出发找到最远的点，这样就得到了最长路径
# 但是这里的距离是欧式距离，所以需要计算平方和，最后再开根号





import init_setting
from lib.cflibs import *

def main(): 
    n = II()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    def dis(i, j):
        x1, y1 = xs[i], ys[i]
        x2, y2 = xs[j], ys[j]
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    
    idx = 0
    for i in range(n):
        if dis(0, i) > dis(0, idx):
            idx = i
    
    st_range = sorted(range(n), key=lambda x: dis(idx, x))
    
    ans = 0
    for i in range(1, n):
        ans += math.sqrt(dis(st_range[i - 1], st_range[i]))
    
    print(ans)