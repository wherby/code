
def TreeMaxPath(g):
    n  = len(g)
    visit =[0]*n
    d =[0]*n
    ans=0
    def dfs(x):
        nonlocal ans
        visit[x] = 1
        for y,c in g[x]:
            if visit[y] : continue
            dfs(y)
            ans = max(ans,d[x] + d[y]  + c)
            d[x] = max(d[x], d[y] + c)
        print(x, d,ans)
    dfs(4)
    return ans
# ./pic/tree.jpg
g = [[(1,3),(2,4),[5,11]],[(3,5),(0,3)],[(4,3),(0,4)],[(1,5)],[(2,3)],[(0,11)]]
ans = TreeMaxPath(g)
print(ans)

