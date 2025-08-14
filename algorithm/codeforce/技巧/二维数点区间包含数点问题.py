# https://codeforces.com/problemset/problem/1896/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0814/solution/cf1896e.md
# 这里求每个点的[startpoint,endpoinr]之间包含了多少个区间，答案就是区间长度- 完整的区间数
# 因为如果 perm[i]<i的时候， 这个点的终点是 n+perm[i],所以把区间倍增
# 要算区间里有多少个区间，把起始端点从右往左遍历，则可以用FenwickTree很好标记
# 但是区间倍增的时候，带来一个问题，如果算[i,n+perm[i]] 区间里的子区间，需要先计算终点位于[0.perm[i]]里的子区间，这样就先后逻辑矛盾了
# 所以这里做了预处理， 因为 perm[i] >=i 的情况，终点在n左边，在预处理的时候，平移了n位，就等于把终点位于[0,perm[i]]的区间先处理了，而本来如果 perm[i] >=i 的时候，终点是小于n的，
# 对结果没有影响，从而解决了前后逻辑矛盾的问题。



import init_setting
from cflibs import *
from lib.fenwicktree import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        perm = LGMI()
        
        ans = [0] * n    
        fen = FenwickTree(2 * n)
        
        for i in range(n):
            if perm[i] >= i:
                fen.add(n + perm[i], 1)
        
        for i in range(n - 1, -1, -1):
            v = perm[i] if perm[i] >= i else perm[i] + n
            ans[perm[i]] = v - i - fen.sum(v)
            #print(i,v, v-i, fen.sum(v))
            fen.add(v, 1)
    
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))

main()

