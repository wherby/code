# https://codeforces.com/gym/102896/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0711/solution/cf102896c.md
# 这里巧妙的是，出现新的子树的时候，旧的子树已经得排列我们其实是去除了，从新的子树开始利用旧的子树顺序构造新的排列
# algorithm/codeforce/docs/联通子图的理想格雷码.md


import init_setting
from lib.cflibs import *
def main():
    n = II()
    parent = [-1] + LGMI()
    
    path = [[] for _ in range(n)]
    for i in range(1, n):
        path[parent[i]].append(i)
    
    def dfs(x):
        ans = []
        for y in path[x]:
            nans = []
            tmp = dfs(y)
    
            nans.extend(tmp)
            for v in ans:
                tmp.reverse()
                nans.append(v)
                nans.extend(tmp)
            
            ans = nans
        
        if x: ans = [x] + ans
        
        return ans
    
    ans = dfs(0)
    
    print(len(ans))
    print(' '.join(str(x + 1) for x in ans))