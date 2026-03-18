# https://codeforces.com/gym/106259/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0317/solution/cf106259f.md
# 均匀分布求期望，用贡献法求期望，对于排序后的区间，有i 个点在左边，n-i 个点在右边，贡献为 (n-i)*i*(a[i]-a[i-1])，最后乘以 2/n 即可
# 如果每个点都与它后面的点连边，则有 n*(n-1)/2 条边，本题中需要连边数量是(n-1) 所以最后需要乘  2/n得到数学期望
#  每条边的权重为 a[j]-a[i]，所以总权重为 sum_{i<j} (a[j]-a[i])，可以转化为 sum_{i=1}^{n} (2*i-n-1)*a[i]，最后乘以 2/n 即可

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    mod = 998244353
    
    for _ in range(t):
        n = II()
        nums = LII()
        nums.sort()
        
        ans = 0
        for i in range(1, n):
            ans = (ans + i * (n - i) * (nums[i] - nums[i - 1])) % mod
        
        outs.append(ans * 2 * pow(n, -1, mod) % mod)
    
    print('\n'.join(map(str, outs)))