import sys

#
# increasing maximum recursion limit to allow recursive dfs on depth trees
#
sys.setrecursionlimit(10**4)

mmpath={}
querdic ={}
def dfs(g, v, p, target, path):
    global querdic,mmpath
    path.append(v)
    if v == target:
        return True
    for u in g[v]:
        if u == p:
            continue
        found = dfs(g, u, v, target, path)
        if found:
            if (u,target) in querdic:
                x = path.index(u)
                mmpath[u,target] = list(path[x:])
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
    global querdic,mmpath
    answers = []
    for u,v in queries:
        querdic[(u,v)] =1
    for u, v in queries:
        path = []
        if (u,v) in mmpath:
            path = mmpath[(u,v)]
        elif (v,u) in mmpath:
            path = reversed(mmpath[(v,u)])
        else:
            dfs(graph, u, -1, v, path)
        odd_path = []
        even_path = []
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