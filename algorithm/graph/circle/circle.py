# lst记录了有向图第i个节点的前驱节点是什么。
def getCircle(lst):
    n = len(lst)
    visited = [0]*n
    cnt = [0]*n
    def dfs(i):
        if visited[lst[i]] ==1:
            cnt[i]  = cnt[lst[i]] +1
        else:
            visited[lst[i]] =1
            cnt[lst[i]]= dfs(lst[i])
            cnt[i]  = cnt[lst[i]] +1
        return cnt[i]
        
    for i in range(n):
        dfs(i)
    mx=0
    for i in range(n):
        # 如果没环，前驱节点和后继节点之间的最大差值是1，如果有环，则是环的长度减一
        mx = max(mx, cnt[lst[i]]-cnt[i]+1)
    print(cnt)
    return mx

re = getCircle( [3,0,1,4,1])
print(re)

## 1-》0-》3-》4-》1