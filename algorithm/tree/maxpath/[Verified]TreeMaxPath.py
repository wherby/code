# verified in  https://leetcode-cn.com/contest/weekly-contest-289/problems/longest-path-with-different-adjacent-characters/
# for [(a,b)] in g , a is the node , b is the weight 
def TreeMaxPath(g):
    n  = len(g)
    ans=0
    visit =[0]*n
    def dfs(x):
        nonlocal ans
        visit[x] = 1
        for y,c in g[x]:
            if visit[y] : continue
            dfs(y)
            ans = max(ans,d[x] + d[y]  + c)
            d[x] = max(d[x], d[y] + c)
        #print(x, d,ans)
    d =[0]*n
    for i in range(n):
        if visit[i] ==0:
            dfs(i)
    return ans


g = [[(1,3),(2,4),[5,11]],[(3,5),(0,3)],[(4,3),(0,4)],[(1,5)],[(2,3)],[(0,11)]]
ans = TreeMaxPath(g)
print(ans)
