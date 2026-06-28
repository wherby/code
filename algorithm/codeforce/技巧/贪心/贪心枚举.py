# https://codeforces.com/gym/106575/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0623/solution/cf106575n.md
# 这里枚举队列 B 中第一个数字放i得到的cost，
# 这时候cur 表示 在B队列放 i 的时候，A 队列第一个数字合法的最小值，
# 这时如果反过来思考，在A队列放入 第 i 个的最小值的时候， B队列 其实可以放 i, i+1,i+2..这样不是不对了吗？ 所以要用枚举B队列的值才能更好解决
# 对于B队列可以放 i, i+1,..的思考也可以这样理解，对于 i+1,...之后的计算，在枚举中也会计算，并且由于A队列的特性，cur在后续的计算中是逐步减少的，所以计算的结果也是完备的



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, ca, cb = MII()
        v1 = LII()
        v2 = LII()
        
        p1 = [0] * n
        p2 = [0] * n
        
        for i in range(n):
            p1[(v1[i] - 1) // 2] = i
            p2[(v2[i] - 1) // 2] = i
        
        ans = 10 ** 18
        cur = n
        
        for i in range(n):
            cur = fmin(cur, p1[i])
            ans = fmin(ans, cur * ca + p2[i] * cb)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))