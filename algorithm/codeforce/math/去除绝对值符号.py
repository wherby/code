# https://codeforces.com/gym/103439/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0323/solution/cf103439n.md
# 因为求值公式是让x,y的值等价，所以把所有点都映射到一个虚拟的轴上？
# 求值公式的值就是在虚拟轴上的点最大值 - 点最小值，所以排序后pair计算就可以了

import init_setting
from cflibs import *
def main(): 
    n = II()
    
    xs = []
    ys = []
    
    for _ in range(n * 2):
        x, y = MII()
        if x > y: x, y = y, x
        xs.append(x)
        ys.append(y)
    
    st_range = sorted(range(2 * n), key=lambda i: xs[i] + ys[i])
    
    print(sum(ys[st_range[2 * n - 1 - i]] - xs[st_range[i]] for i in range(n)))