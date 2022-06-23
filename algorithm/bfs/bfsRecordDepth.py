from collections import deque
def bfs(g,stp):
    n = len(g)
    d =[0]*n # depth
    st =deque([stp])
    d[stp] = 1
    while st:
        p = st.popleft()
        for a in g[p]:
            if d[a]:continue
            d[a] = d[p]+1
            st.append(a)
    return d