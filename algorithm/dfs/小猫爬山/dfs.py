


from turtle import pen


def dfs(now,cnt):
    global ans,n,w
    #print(now,cnt,cab)
    if cnt>= ans:
        return
    if now == n:
        #print(cab,cnt,ans)
        ans = min(ans,cnt)
        return
    for i in range(cnt):
        if cab[i] + cat[now] <=  w:
            cab[i] += cat[now]
            dfs(now +1, cnt)
            cab[i] -= cat[now]
    cab[cnt +1] =cat[now]
    dfs(now +1, cnt +1)
    cab[cnt+1] =0
    
ans = 10**9
w = 10
cat = [1,2,3,4,5,6,7,8,9,10,5]
n = len(cat)
cab = [0]*n
dfs(0,0)
print(ans+1)