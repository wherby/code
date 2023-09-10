# https://oi-wiki.org/graph/dsu-on-tree/
#给出一棵 n 个节点以 1 为根的树，节点 u 的颜色为 c_u，
# 现在对于每个结点 u 询问 u 子树里一共出现了多少种不同的颜色。




N = 10**5 *2+5

## InputVal
col = [0]*N
g = [[] for _ in range(N)]
## endInputVal

sz= big = L = R = Node = [0]*N
totdfn = 0 
ans =cnt =[0]*N 
totcol = 0



def add(u):
    global totcol
    if cnt[col[u]] ==0:
        totcol +=1
    cnt[col[u]] +=1

def delete(u):
    global totcol
    cnt[col[u]] -=1
    if cnt[col[u]] == 0 :
        totcol -=1

def getAns():
    return totcol

def dfs0(u,p):
    global totdfn
    totdfn +=1
    L[u] = totdfn
    Node[totdfn] = u 
    sz[u] =1
    for v in g[u]:
        if v != p:
            dfs0(v,u)
        sz[u] += sz[v]
        if big[u] == 0 or sz[big[u]] < sz[v]:
            big[u] = v 
    R[u] = totdfn
    
def dfs1(u,p,keep):
    # 计算轻儿子的答案
    for v in g[u]:
        if v != p and v != big[u]:
            dfs1(v,u,False)
    # 计算重儿子答案并保留计算过程中的数据（用于继承）
    if big[u]:
        dfs1(big[u],u,True)
    for v in g[u]:
        if v !=p and v != big[u]:
            # 子树结点的 DFS 序构成一段连续区间，可以直接遍历
            for i in range(L[v],R[v]+1):
                add(Node[i])
    add(u)
    ans[u] = getAns(u)
    if keep == False:
        for i in range(L[u],R[u]+1):
            delete(Node[i])


## get input for col and g 
## col
## g 
## node number start from 1
dfs0(1,0)
dfs1(1,0,False)
for i in range(N):
    print(ans[i])