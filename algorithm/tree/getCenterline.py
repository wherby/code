# https://leetcode.cn/contest/weekly-contest-404/problems/find-minimum-diameter-after-merging-two-trees/description/
# contest\00000c397d130\c404\q4\t4.py
# 得到最中心的线段


from collections import defaultdict,deque

def getCenter2(edges):
    ind = defaultdict(int)
    g= defaultdict(list)
    for a,b in edges:
        ind[a]+=1
        ind[b]+=1
        g[a].append(b)
        g[b].append(a)
    cand = []
    for k in ind.keys():
        if ind[k] ==1:
            cand.append(k)
    n = len(ind.keys())
    if n<=2:
        return cand
    visit={}
    while cand:
        tmp = []
        for a in cand:
            visit[a] =1
            for b in g[a]:
                if b not in visit:
                    ind[b] -=1
                    if ind[b] == 1:
                        tmp.append(b)
        cand = tmp
        if len(visit) >=n-2:
            return cand