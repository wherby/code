# https://codeforces.com/gym/103821/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0707/solution/cf103821k.md
# 使用贡献法标记的，左右分别在不同的坐标上标记。右边标记可以用作为尾部的情况下有多少种可能
# 左边标记当前节点作为起点的时候有多少种可能，
# 这里使用的扫描线法，扫描点表示两段中间的间隔点，从右到左扫描，如果当前是左端点，则表示右端点的贡献值可以被释放，累积到左边所以的端点都能使用。
# 如果扫描点是右端点，则可以计算此时当前左端点能与累积的右端点有多少个组合贡献


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n, m = MII()
        
        tmp1 = [0] * (m + 1)
        tmp2 = [0] * (m + 1)
        
        for _ in range(n):
            l, r = MII()
            tmp1[l] += m + 1 - r
            tmp2[r] += l
        
        ans = 0
        total = 0
        
        for i in range(m, 0, -1):
            ans = (ans + tmp2[i] * total) % mod
            total = (total + tmp1[i]) % mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))