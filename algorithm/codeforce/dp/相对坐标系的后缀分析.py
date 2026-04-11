# https://codeforces.com/gym/106463/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0408/solution/cf106463a.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0408/personal_submission/cf106463a_yawn_sean.py
# algorithm/codeforce/docs/后缀DP分析/剥洋葱式分析跳跃路径/公式推导.md
# algorithm/codeforce/docs/后缀DP分析/剥洋葱式分析跳跃路径/输入分析.md
# 剥洋葱方式从后往前看
# 从后往前分析，动态规划和路径压缩
# 从后往前记录在相对坐标系下，需要再移动积累到多少才会再撞 “坑” ，因为从后往前，所以可以知道后面有没有这个
# 需要的积累数
# 如果知道后面的最近撞坑的index,则直接查询撞坑之后的最后值，这里用到了路径压缩，如果没有撞坑，则平凡计算
# 遍历所有移动之后就知道了在相对坐标系下，任意一点最近的撞坑index，或者不撞则平凡情况求解


import init_setting
from lib.cflibs import *
# Submission link: https://codeforces.com/gym/106463/submission/370070663
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, k, x, y = MII()
        nums = LII()
        
        for i in range(1, k):
            nums[i] = (nums[i] + nums[i - 1]) % n
        
        vis = [-1] * n
        target = [0] * k
        
        for i in range(k - 1, -1, -1):
            to_find_pos = (nums[i] + (x - y)) % n
            target[i] = target[vis[to_find_pos]] if vis[to_find_pos] != -1 else (y + nums[-1] - nums[i]) % n
            vis[nums[i]] = i
        
        ans = []
        for i in range(n):
            if i != x:
                to_find_pos = (x - i) % n
                ans.append(target[vis[to_find_pos]] if vis[to_find_pos] != -1 else (i + nums[-1]) % n)
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))