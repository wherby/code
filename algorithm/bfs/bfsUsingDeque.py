# BFS
# https://leetcode-cn.com/problems/minimum-height-trees/

from collections import deque

def bfs(g,stp):
    n = len(g)
    visited =[0]*n
    st =deque([(stp,0)])
    ret = []
    while st:
        p,layer = st.popleft()
        visited[p] =1
        for a in g[p]:
            if visited[a]:continue
            st.append((a,layer+1))
        ret.append((p,layer))
    return ret