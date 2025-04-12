# algorithm/codeforce-etcs/dfs中排序.py

```python
while stk:
    u = stk.pop()
    if u >= 0:
        if u > 0:
            ans.append(parent[u])
        stk.append(~u)
        path[u].sort(key=lambda x: -vis[x])
        for v in path[u]:
            if parent[v] == u:
                stk.append(v)
    else:
        ans.append(~u)
```