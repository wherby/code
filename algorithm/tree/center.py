# Center of gravity ./pic/center.png 树的重心
#定义1：找到一个点，其所有的子树中最大的子树节点数最少，那么这个点就是这棵树的重心。
#定义2：以这个点为根，那么所有的子树（不算整个树自身）的大小都不超过整个树大小的一半。
#性质1：树中所有点到某个点的距离和中，到重心的距离和是最小的；如果有两个重心，那么他们的距离和一样。
#性质2：把两个树通过一条边相连得到一个新的树，那么新的树的重心在连接原来两个树的重心的路径上。
#性质3：把一个树添加或删除一个叶子，那么它的重心最多只移动一条边的距离
# https://oi-wiki.org/graph/tree-centroid/
# 树的重心和树的直径没有任何关系，如果树是一个菊花形状子树和长链结合。则重心在菊花子树上，直径是长链上

def dfs(x):
    global ans,pos
    v[x] =1
    size[x] =1
    max_part =0
    for y in g[x]:
        if v[y] : continue
        dfs(y)
        size[x] += size[y]
        max_part  = max(max_part,size[y])
    max_part = max(max_part,n - size[x])
    if max_part < ans:
        ans = max_part
        pos = x



g =[[] for _ in range(10)]
g[1]=[2,7,4]
g[2]= [8,5]
g[4] = [3,6]
g[3] =[9]
n =9
v = [0]*10
size = [0]*10
ans =10
pos = -1
dfs(1)
print(ans,pos)