# https://codeforces.com/gym/106020/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0626/solution/cf106020c.md
# 这里的问题是把树分成两部分之后，其中一部分能不能是GCD等于1，
# 这里的问题就是整体的GCD为1 的时候，有没有分割点可以得到其中一个为1的分割方法， 但是这样求的代价太高，反向思考，
# 如果有分割点可以得到两个部分的GCD都不为1，则这两部分的GCD互质，如果树上能找到16个分割点，则16 个互质的因子就超过了最大值
# algorithm/codeforce/docs/GCD因子互斥.md 
# 在链的时候，只判断了端点，为什么就可以了？端点可以代表了链上点到端点的所有情况(GCD单调性)  algorithm/codeforce/docs/GCD因子互斥端点的特点.md
# 题目采用了重排序的方式，让叶子节点在最前面



import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import SegTree
def main():
    n = II()
    nums = LII()
    
    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    tmp = []
    for i in range(n):
        if len(path[i]) == 1:
            tmp.append(i)
    
    for i in range(n):
        if len(path[i]) > 1:
            tmp.append(i)
    
    vals = [0] * n
    pos = [0] * n
    
    for i in range(n):
        vals[i] = nums[tmp[i]]
        pos[tmp[i]] = i
    
    seg = SegTree(math.gcd, 0, vals)
    
    q = II()
    outs = []
    
    for _ in range(q):
        i, x = MII()
        i -= 1
        
        vals[pos[i]] = x
        seg.set(pos[i], x)
        
        k = fmin(16, n)
        val = seg.prod(k, n)
        
        pref = [0]
        for i in range(k - 1):
            pref.append(math.gcd(pref[-1], vals[i]))
        
        flg = False
        for i in range(k - 1, -1, -1):
            if len(path[tmp[i]]) == 1 and math.gcd(pref[i], val) == 1:
                flg = True
            val = math.gcd(vals[i], val)
        
        outs.append('Yes' if flg else 'No')
    
    print('\n'.join(outs))