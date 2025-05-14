

## BFS use queue
algorithm/codeforce/bfsUsingQueue.py
algorithm/bfs/BFSQueue.py
这里在循环中改变了容器内容
```python
    for u in que:
        for v in path[u]:
            if dis1[v] == -1:
                dis1[v] = dis1[u] + 1
                que.append(v)
```

## Return value 
algorithm/codeforce/BFS最短路.py
```python 
            for x in range(10):
                if cnt[x] and dis[x] == 10:
                    break
                res += cnt[x] * dis[x]
            else:
                ans[i][j] = res
```

关键点解析
for-else 结构：
else 子句会在循环正常完成（即没有被 break 中断）时执行。
如果循环被 break 中断，else 部分不会执行。
循环逻辑：
遍历 x 从 0 到 9（range(10)）。
检查两个条件：
cnt[x] 是否为真（即非零、非空、非 False）。
dis[x] 是否等于 10。
如果两个条件同时满足，则执行 break，退出循环。
否则，将 cnt[x] * dis[x] 的值累加到 res 中。
else 子句：
如果循环完整执行（没有触发 break），则将 res 的值赋给 ans[i][j]。
逻辑总结
这段代码的目的是遍历 x 从 0 到 9，并在过程中检查是否存在某个 x 满足 cnt[x] 为真且 dis[x] == 10。
如果存在这样的 x，则立即终止循环，且不执行 else 部分的赋值操作。
如果不存在这样的 x，则循环会完整执行，并将累加结果 res 赋值给 ans[i][j]。