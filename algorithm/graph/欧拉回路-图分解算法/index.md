

## 原图是没有欧拉回路的处理方式

[处理图形输出欧拉回路](euler_tour.question1.py)

```python
    for _ in range(m):
        u, v = GMI()
        deg[u] += 1
        deg[v] += 1
        us.append(u)
        vs.append(v)
    
    cur = -1
    
    for i in range(n):
        if deg[i] % 2:
            if cur != -1:
                us.append(cur)
                vs.append(i)
                cur = -1
            else:
                cur = i
```
如果点的度是奇数，则找到另一奇数点，连接虚拟线段，使得图内所有点都是偶数点，让图可以分解为欧拉回路的图


处理欧拉回路的划分： 如果回路的连接数是偶数，则可以随便划分， 
                  如果是奇数，而且有虚拟线段，则可以从虚拟线段处断开,从而使得开头和结尾是虚拟线段
                  如果是奇数，切没有虚拟线段，则从最小损失点断开。
```python
        if len(eids) % 2 == 0:
            for eid in eids[::2]:
                col[eid] = 2
        elif max(eids) >= m:
            v = eids.index(max(eids))
            eids = eids[v+1:] + eids[:v]
            for eid in eids[::2]:
                col[eid] = 2
        else:
            u = tour[0]
            for x in tour:
                if deg[x] < deg[u]:
                    u = x
            
            v = eids.index(u)
            eids = eids[v+1:] + eids[:v]
            for eid in eids[::2]:
                col[eid] = 2
```
"v = eids.index(u)" 这里有问题？？


## 欧拉路径构成方法

[欧拉路径构成方法](plan_out_satwik_sinha_source_code.cpp)

如果原图没有办法构成欧拉路径，则建立一个虚拟节点，如果点是奇数度，则虚拟节点和它连接一次，如果是偶数度，则虚拟节点与之连接两次，这样图内所有节点都是互相连接，且所有度都是偶数，则图可以有一条欧拉路径访问完成。

这里做了优化，如果联通区域没有边，则不需要和虚拟节点连接，如果联通区域有奇数边，则也不需要连接，因为区域在奇数边的时候已经连接完成
```cpp
        vector<int> rep(n, -1), hasEdge(n, 0), hasOdd(n, 0);
        for (int v = 0; v < n; v++) {
            if (deg[v] > 0) {
                int r = dsu.find(v);
                hasEdge[r] = 1;
                if (rep[r] == -1) rep[r] = v;
                if (deg[v] & 1) hasOdd[r] = 1;
            }
        }
        for (int r = 0; r < n; r++) {
            if (hasEdge[r] && !hasOdd[r]) {
                int v = rep[r];
                add_edge(v, S, -1);
                add_edge(v, S, -1);
            }
        }
```
为什么经过虚拟节点的连接不影响奇偶性？ 因为虚拟节点的度一定是偶数，且因为是欧拉路径出入pair是一起的