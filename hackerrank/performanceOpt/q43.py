import sys

#
# increasing maximum recursion limit to allow recursive dfs on depth trees
#
sys.setrecursionlimit(10**4)

mmpath={}
querdic ={}
maxb = 14
lca = []
dfscnt =0
maxn = 22020
indfs = [0]*maxn
outdfs =[0]*maxn
dep = [0]*maxn
for i in range(maxn):
    tp = [0]*maxb
    lca.append(tp)

dfsord = [0]*maxn

init = False

def dfsNew(g,u,fa,d):
    global dfscnt,indfs,outdfs,maxb,dep
    dfscnt = dfscnt +1
    indfs[u] = dfscnt   
    lca[u][0] = fa 
    dep[u] = d
    for i in range(1,maxb):
        f = lca[u][i-1]
        lca[u][i] =lca[f][i-1]
    for v in g[u]:
        if v == fa:
            continue
        dfsNew(g,v,u,d+1)
    dfscnt = dfscnt +1
    outdfs[u] = dfscnt
    
def LCA(u,v):
    global dep,maxb,lca
    if dep[u] < dep[v]:
        t= u
        u =v
        v=t
    for i in range(maxb-1,-1,-1):
        if dep[lca[u][i]] >= dep[v]:
            u =lca[u][i]
    if u == v:
        return u
    for i in range(maxb -1,-1,-1):
        if lca[u][i] != lca[v][i]:
            u=lca[u][i]
            v = lca[v][i]
    return lca[u][0]

def dfs(g, v, p, target, path):
    global querdic,mmpath,init,maxn,dfsord,indfs,outdfs
    if v == target:
        return 
    if init == False:
        dfsNew(graph,0,maxn-1,1)
        init = True
        n =len(g)
        for i in range(n):
            dfsord[indfs[i]] =i
            dfsord[outdfs[i]] =i
        #print dfsord[: n*2+1]
    #print "v=" +str(v) + "   target = "+ str(target)
    if LCA(v,target) == v:
        path1 = dfsord[indfs[v]:indfs[target] +1]
    elif LCA(v,target)==target:
        path1 = list(reversed(dfsord[indfs[target]:indfs[v]+1]))
    else:
        p = LCA(v,target)
        if indfs[v] < indfs[target]:
            path1= list(reversed(dfsord[indfs[p]:indfs[v]+1]))
            path2 = list(reversed(dfsord[outdfs[target]:outdfs[p]]))
            path1.extend(path2)
            
        else:
            path1 = list(dfsord[outdfs[v]:outdfs[p]])
            path2 = list(dfsord[indfs[p]:indfs[target]+1])
            path1.extend(path2) 
    nn = len(path1)
    re = []
    for i in range(nn):
        if i >1 and path1[i] == re[-1]:
            re= re[:len(re)-1] 
        else:
            re.append(path1[i])      
    path.extend(re)
    #print path
    

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
    
