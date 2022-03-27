inD=[0]*26
graph={}
from collections import deque


def orderVisit():
    st= deque([])
    res =[]
    for k,_ in graph:
        if inD[k] ==0:
            st.append(k)
    while st:
        t = st.popleft()
        res.append(t)
        for a in graph[t]:
            inD[a] -=1
            if inD[a] ==0:
                st.append(a)
    return res