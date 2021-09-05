import sys
#
# increasing maximum recursion limit to allow recursive dfs on depth trees
#
sys.setrecursionlimit(10**4)
mmpath = []
def dfs(g, v, p, target, path):
    global mmpath
    n = len(mmpath)
    for i in range(n):
        dic1,pathT = mmpath[i]
        if v in dic1 and target in dic1:
            if pathT[dic1[v]] < pathT[dic1[target]]:
                ttpath = pathT[dic1[v]:dic1[target]+1]
            else:
                ttpath =pathT[dic1[target]: dic1[v] +1]
                ttpath = reversed(ttpath)
            if len(path) >1:
                path = path.extend(ttpath[1:])
            else:
                path = path.extend(ttpath)
            return True
    path.append(v)
    if v == target:
        return True
    for u in g[v]:
        if u == p:
            continue
        found = dfs(g, u, v, target, path)
        n = len(path)
        #print path
        dic1 = {}
        if found:
            for i in range(n):
                dic1[path[i]] = i
                mmpath.append([dic1,list(path)])
            return True
    path.pop()
    return False

#
# Kadane's algorith: https://en.wikipedia.org/wiki/Maximum_subarray_problem
#
def kadane(a):
    if len(a) == 0:
        return 0
    max_ending_here = max(a[0], 0);
    max_so_far = max_ending_here;
    for i in xrange(1, len(a)):
        max_ending_here = max(max(0, a[i]), max_ending_here+a[i]);
        max_so_far = max(max_so_far, max_ending_here);
    return max_so_far;

def skippingSubpathSum(n, c, graph, queries):
    answers = []
    for u, v in queries:
        path = []
        dfs(graph, u, -1, v, path)
        odd_path = []
        even_path = []
        #print u,v ,path
        for i in xrange(len(path)):
            if (i+1)%2 == 0:
                even_path.append(c[path[i]])
            else:
                odd_path.append(c[path[i]])
        s1 = kadane(even_path)
        s2 = kadane(odd_path)
        answers.append(max(s1, s2))
    return answers


if __name__ == "__main__":
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    graph = [[] for _ in xrange(n)]
    for _ in xrange(n-1):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
        graph[v].append(u)
    q = int(raw_input().strip())
    queries = []
    for _ in xrange(q):
        u, v = map(int, raw_input().split())
        queries.append((u, v))
    answers = skippingSubpathSum(n, c, graph, queries)
    print "\n".join(map(str, answers))  
    #print mmpath