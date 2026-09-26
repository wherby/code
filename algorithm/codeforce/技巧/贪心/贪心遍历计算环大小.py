# https://codeforces.com/gym/106722/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0926/solution/cf106722d.md
# 贪心遍历所有节点的时候，就能找到最小环大小
# 这里没有必要用二分求环大小，
# 这里双向遍历可以想象二维平面的梯度下降寻路

import init_setting
from cflibs import *
def main():
    def query(i, step):
        print('?', i, step, flush=True)
        return I() == 'Yes'
    
    n = II()
    
    cycle_size = n
    
    for i in range(1, n + 1):
        while cycle_size > 1 and query(i, cycle_size - 1):
            cycle_size -= 1
    
    ans = []
    
    for i in range(1, n + 1):
        if query(i, cycle_size):
            ans.append(i)
    
    print('!', len(ans), ' '.join(map(str, ans)))