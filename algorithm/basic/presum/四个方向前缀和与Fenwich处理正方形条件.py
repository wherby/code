# https://codeforces.com/gym/104072/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1017/solution/cf104072d.md
# 四个方向处理前缀问题
# 然后在对角线上处理，左上和右下的合并最大值
# 处理对角线匹配问题:
#               1，用tmp 记录右下端点起始的index位置，里面的值就是右下端点的index J 对应于终止位置
#               2. 在 i循环的时候，激活起始位置开始的点，在fenwick 上标记结束点(J) 查询 另一参数 i + v1[i] 就是当前参数终止的位置
#               3. ans += fen.sum(i + v1[i]) 这里计算的是 0 到 i+v1[i] 之间的值，在i点，只有i到 i +v1[i]是有意义的，但是当前激活对的是 i开始的值，所以最后需要减去 ans - k * (k - 1) // 2  
#                       为什么是k * (k - 1) // 2 ，因为不论怎么激活分布 J 的分布都是 1。。K， 
#                  如果这里写成 ans += fen.rsum(i,i + v1[i]) 计算之间有效值，则不用多余的减去值 
#                  遍历在i点激活另一维度从i开始的参数，这样可以保证在查询时fenwick里记录的数据是有效的，同时激活的时候记录了在树上的结束端点
#              所以Fenwick 树可以用来记录结束影响值，开始的值用遍历的方式激活 用线段树也可以达到一样的效果
# 用FenWick Tree 解决的问题思路：
#  原问题是两类统计量，一个是在当前坐标往左，一个是当前坐标往右 的区间，求这两类统计量的重合数量
#   把坐标往左的统计量用 i - v2[i] 找到最左坐标，然后记录终止坐标， 其实是把此统计量变成了坐标往右的统计量了
#   然后用fenwickTree 依次激活起始值为当前的一个统计量，用另一个统计量的有效值区间查询
#
                
                



import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree
def main(): 
    n = II()
    grid = [LII() for _ in range(n)]
    
    u = [x[:] for x in grid]
    d = [x[:] for x in grid]
    l = [x[:] for x in grid]
    r = [x[:] for x in grid]
    
    for i in range(1, n):
        for j in range(n):
            if u[i][j]:
                u[i][j] = u[i - 1][j] + 1
    
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if d[i][j]:
                d[i][j] = d[i + 1][j] + 1
    
    for i in range(n):
        for j in range(1, n):
            if l[i][j]:
                l[i][j] = l[i][j - 1] + 1
    
    for i in range(n):
        for j in range(n - 2, -1, -1):
            if r[i][j]:
                r[i][j] = r[i][j + 1] + 1
    
    def solve(x, y):
        v1 = []
        v2 = []
        
        while x < n and y < n:
            v1.append(fmin(d[x][y], r[x][y]) - 1)
            v2.append(fmin(u[x][y], l[x][y]) - 1)
            x += 1
            y += 1
        
        k = len(v1)
        
        ans = 0
        
        fen = FenwickTree(k + 1)
        tmp = [[] for _ in range(k + 1)]
        
        for i in range(k):
            tmp[i - v2[i]].append(i)
        
        for i in range(k):
            for j in tmp[i]:
                fen.add(j, 1)
            ans += fen.sum(i + v1[i])
        return ans - k * (k - 1) // 2
    
    ans = solve(0, 0)
    for i in range(1, n):
        ans += solve(0, i) + solve(i, 0)
    
    print(ans)

main()