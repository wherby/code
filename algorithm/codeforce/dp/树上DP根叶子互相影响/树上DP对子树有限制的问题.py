# https://codeforces.com/gym/102861/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0915/solution/cf102861i.md

# dp0[i]: 以i为根的子树中，最终有一个未知节点的方案数
# dp1[i]: 以i为根的子树中，所有节点都已知的方案数

# 那么：
# v0: 当前已合并的子树中，有一个未知节点的方案数
# v1: 当前已合并的子树中，所有节点都已知的方案数

# 这样：
# dp0[i] = v0: 如果不查询i，且子树中有一个未知节点
# dp1[i] = v0 + v1: 如果查询i，那么所有节点都已知
# 这种解释更合理，也符合"每棵子树不可能有两个元素不确定数值"的提示。
# 所以初始化为 v0 = 0, v1 = 1 是合理的：

# 还没有子节点时：有未知节点 (v0 = 0)，所有节点已知 (v1 = 1)

# dp0, dp1 同时表示了是否查询当前根节点之后，当前子树的状态  ： dp0[i] = v0: 如果不查询i，且子树中有一个未知节点 如果不查询当前根节点，则当前子树就会一直保持有一个节点未知
#                                                       dp1[i] = v0 + v1: 如果查询i，那么所有节点都已知 如果查询了当前根节点，则当前子树有一个节点未知的情况就解决了，当前子树所有节点都变成已知，
#                                                      这里dp0 虽然是不查询根节点的状态，当时的分析是因果倒置， 因为你要让当前子树有未知的一个节点，你能做的事情是一定不要查询根节点，并且子树有一个未知节点， 
#                                                                  但是在定义状态的时候，我们不认为dp0 是不查询根节点的”因“，我们只需要让这个子树有一个未知状态，则一定是根节点不查询


import init_setting
from lib.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7
    
    parent = [-1] + LGMI()
    
    path = [[] for _ in range(n)]
    for i in range(1, n):
        path[parent[i]].append(i)
    
    que = [0]
    for i in que:
        for j in path[i]:
            que.append(j)
    
    que.reverse()
    
    dp0 = [1] * n
    dp1 = [1] * n
    
    for i in que:
        if len(path[i]) == 0:
            continue
        
        v0, v1 = 0, 1
        
        for j in path[i]:
            v0 = (v1 * dp0[j] + v0 * dp1[j]) % mod
            v1 = v1 * dp1[j] % mod
        
        dp0[i] = v0
        dp1[i] = (v0 + v1) % mod
        
    print(dp1[0])