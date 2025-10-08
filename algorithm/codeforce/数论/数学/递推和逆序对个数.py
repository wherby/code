# 
# https://codeforces.com/gym/106100/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1007/solution/cf106100f.md
# 把一个数字从后到前依次交换就会发现这个数字在位置上等于 a-i，
# 因为有等值的数字，为了得到最小对的交换，所以d记录每个数字的index,v2的时候从后到前遍历得到每个数字的最后一次出现的index，这样得到的编码同一数字没有区间重叠
# 逆序对用从后到前用线段树查询 区间逆序数字对数


import init_setting
from cflibs import *
def main():
    n = II()
    v1 = LII()
    v2 = LII()
    
    for i in range(n):
        v1[i] -= i
        v2[i] -= i
    
    if sorted(v1) != sorted(v2):
        print(-1)
    else:
        rnd = random.getrandbits(30)
        d = defaultdict(list)
        
        for i, v in enumerate(v1):
            d[v ^ rnd].append(i)
        
        for i in range(n - 1, -1, -1):
            v2[i] = d[v2[i] ^ rnd].pop()
        
        fen = FenwickTree(n)
        
        ans = 0
        for i in range(n):
            ans += fen.rsum(v2[i], n - 1)
            fen.add(v2[i], 1)
        
        print(ans)