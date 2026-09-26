# https://codeforces.com/gym/102760/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0826/solution/cf102760k.md
# 这里需要构造图形不相交，所以坐标系排序构造出的连接曲线也是不互相相交的联通图形
# 这里排序的奇数位置和偶数位置对应正反图，而这里的构造方式能保证奇数和偶数都能得到完整集
# 距离5个点 s1,s2,s3,s4,s5,s4,s3,s2,s1
# (s1,s2),(s2,s3),(s3,s4),(s4,s5),(s5,s4),(s4,s3),(s3,s2),(s2,s1)
# 偶数位置：(s1,s2) (s3,4) (s5,s4) (s3,s2)
# 奇数位置：(s2,s3) (s4,s5) (s4,s3) (s2,s1)


import init_setting
from lib.cflibs import *
def main():
    n = II()
    pts = [tuple(MII()) for _ in range(n)]
    
    order = sorted(range(n), key=lambda x: pts[x])
    for i in range(n - 2, -1, -1):
        order.append(order[i])
    
    print(2 * n - 1)
    print(' '.join(str(x + 1) for x in order))