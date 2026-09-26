# https://codeforces.com/gym/101798/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0922/solution/cf101798h.md
# 这里使用多源BFS 同步求出上下两个环的所有节点
# 但是由于一个起点的时候，有两个可能的方向，这时怎么让两个环匹配？ algorithm/codeforce/图论/docs/index重排匹配节点.md   《=解决了如何确定两个等长的环的相对位置是顺序连接的判定？ 
# 这里有多个检测： 如果确定是两个等长的闭合环？ 



import init_setting
from cflibs import *
def main():
    n = II()
    path = [[] for _ in range(n)]
    
    for _ in range(n // 2 * 3):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    if any(len(path[i]) != 3 for i in range(n)): print('NO')
    else:
        def check(x, y):
            que = [x, y]
            
            dis = [-1] * n
            dis[x] = 0
            dis[y] = 0
            
            npath = [[] for _ in range(n)]
            
            for u in que:
                for v in path[u]:
                    if dis[v] == -1:
                        dis[v] = dis[u] + 1
                        npath[u].append(v)
                        npath[v].append(u)
                        que.append(v)
            
            for i in range(n):
                if len(npath[i]) > 2: return
            
            vis = [0] * n
            chains = []
            
            for i in range(n):
                if not vis[i] and len(npath[i]) == 1:
                    chain = [i]
                    vis[i] = 1
                    
                    for u in chain:
                        for v in npath[u]:
                            if not vis[v]:
                                vis[v] = 1
                                chain.append(v)
                    
                    chains.append(chain)
            
            if len(chains) != 2 or len(chains[0]) != n // 2 or len(chains[1]) != n // 2: return
            if chains[0][0] not in path[chains[0][-1]]: return
            if chains[1][0] not in path[chains[1][-1]]: return
            
            idxs = [-1] * n
            for i in range(n // 2):
                idxs[chains[0][i]] = i
            
            tmp = []
            for i in range(n // 2):
                u = chains[1][i]
                chosen = -1
                
                for v in path[u]:
                    if idxs[v] != -1:
                        chosen = idxs[v]
                
                if chosen == -1: return
                tmp.append(chosen)
            
            diff = (tmp[1] - tmp[0]) % (n // 2)
            
            if diff != 1 and diff != n // 2 - 1: return
            
            for i in range(1, n // 2):
                if (tmp[i] - tmp[i - 1]) % (n // 2) != diff:
                    return
            
            print('YES')
            print(' '.join(str(x + 1) for x in chains[1]))
            print(' '.join(str(chains[0][x] + 1) for x in tmp))
            exit()
        
        for v in path[0]:
            check(0, v)
        
        print('NO')