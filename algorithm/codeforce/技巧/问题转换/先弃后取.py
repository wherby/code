# https://codeforces.com/gym/106646/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1024/solution/cf106646h.md
# 这里其实  Sum(V1 of selectIdx) - Sum(v2 of unSelectIndex) 
# 这里先把v1中 selectIdx 都一起去掉，则变成 Sum((v1+v2) of selectIdx) - Sum(v2) 
# 就变成了一个贪心求极值的问题， 而因为需要先选才能丢弃，所以在 i%2的时候，最少要选择一个值才能满足当前选择大于等于丢弃的个数



import init_setting
from lib.cflibs import *
def main():
    n = II()
    v1 = LII()
    v2 = LII()
    
    ans = 0
    pq = []
    
    for i in range(2 * n):
        ans -= v2[i]
        heappush(pq, -(v1[i] + v2[i]))
        if i % 2 == 0: ans -= heappop(pq)
    
    print(ans)