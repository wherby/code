# https://codeforces.com/gym/106391/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0302/solution/cf106391b.md
# 用抽屉原理得知一定能满足条件
# 每次选择两个点构成边
# 而抽屉原理得知，一定可以两条边，如果都从低往高排列，则低点一定是连通区域、、、、
# 证明？ 因为1的时候，1,2 连接，则2的时候，1,2，必然与3 连接，或者1,2 连接， 如此类推，则新的点一定与1的联通区域连接


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        used = [0] * n
        
        outs.append('YES')
        ops = []
        
        for i in range(n - 1, 0, -1):
            vis = [-1] * i
            
            for j in range(n):
                if not used[j]:
                    x = nums[j] % i
                    if vis[x] != -1:
                        used[j] = 1
                        ops.append(f'{vis[x] + 1} {j + 1}')
                        break
                    vis[x] = j
        
        outs.append('1')
        ops.reverse()
        outs.append('\n'.join(ops))
    
    print('\n'.join(outs))