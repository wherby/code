# https://codeforces.com/gym/106670/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0827/solution/cf106670k.md
# 枚举可能的路径？ 
# 其实是已知起始点和终点两个点一定在路径上，这时这两点有4种选择，再在这4种选择中枚举可能的连接方式
# 枚举可能的“连接方式”



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        v1 = LII()
        v2 = LII()
        
        outs.append(min(
            v1[0] + v2[n - 1],
            v2[0] + v1[n - 1],
            sum(v1),
            sum(v2),
            v1[0] + v1[n - 1] + min(v2),
            v2[0] + v2[n - 1] + min(v1)
        ))
    
    print('\n'.join(map(str, outs)))