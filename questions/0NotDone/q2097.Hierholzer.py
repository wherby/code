# https://leetcode.com/contest/weekly-contest-270/problems/valid-arrangement-of-pairs/

from collections import defaultdict
class Solution(object):
    def validArrangement(self, pairs):
        dic = {}
        g= defaultdict(list)
        
        for a,b in pairs:
            if a not in dic:
                dic[a] = [0,0]
            if b not in dic:
                dic[b] = [0,0]
            dic[a][0] +=1
            dic[b][1] +=1
        for i,p in enumerate(pairs):
            g[p[0]].append(p[1])

        cand = []
        for k,v in dic.items():
            if v[0]>v[1]:
                cand.append(k)
        start = pairs[0][0]
        if len(cand) >0:
            start =cand[0]
        # Hierholzer's Algorithm:
        def visit(start,g):
            st = [start]
            route=[]
            while st:
                while g[st[-1]]:
                    st.append(g[st[-1]].pop())
                route.append(st.pop())
            route.reverse()
            return [[route[i], route[i+1]] for i in range(len(route)-1)]
        return visit(start,g)