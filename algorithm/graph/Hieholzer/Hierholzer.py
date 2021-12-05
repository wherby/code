# https://www.youtube.com/watch?v=Az2HUuB3IB4
# 一笔画问题
#https://leetcode.com/problems/valid-arrangement-of-pairs/discuss/1611983/Python-O(pairs.length)-Hierholzer's-Algorithm 
# g: graph  start point[inbound > outbound]
# TDK Hierholzer
def visit(start,g):
    st = [start]
    route=[]
    while st:
        while g[st[-1]]:
            st.append(g[st[-1]].pop())
        route.append(st.pop())
    route.reverse()
    return [[route[i], route[i+1]] for i in range(len(route)-1)]
