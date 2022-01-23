# Center of gravity ./pic/center.png

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