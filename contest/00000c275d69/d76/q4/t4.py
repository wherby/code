class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append((scores[b],b))
            g[b].append((scores[a],a))
        mx =-1
        for i in range(n):
            g[i].sort(reverse=True)
        for a,b in edges:
            if len(g[a]) ==1 or len(g[b]) ==1:continue
            s1 = set([a,b])
            l1 = g[a][:3]
            l2 = g[b][:3]
            for c1,c in l1:
                for d1,d in l2:
                    if c != d and (c not in s1) and (d not in s1):
                        mx = max(mx,scores[a]+scores[b] + c1+d1)
        return mx