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
        return path.extend([[indfs[v],indfs[v]+1]])  #return   return path.extend([target])  #BUG: if v == target should return No
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
        path1 = [[indfs[v],indfs[target] +1]]
    elif LCA(v,target)==target:
        path1 = [[outdfs[v],outdfs[target]+1]]
    else:
        p = LCA(v,target)
        path1 =[[outdfs[v],outdfs[p]]]
        path2 = [[indfs[p],indfs[target]+1]]
        path1.extend(path2)  
    path.extend(path1)
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
    return max_so_far

def rangeCompare(A,B):
    if A[0]/100 != B[0]/100:
        return A[0]/100 - B[0]/100
    return A[1] - B[1]

def getAllRanges(allquerys):
    from collections import deque
    global dfsord
    dfsord[0]=-1
    #print dfsord[:30]
    dic1 = {}
    query0= allquerys[0]
    curL=0
    curR=0
    n = len(allquerys)
    A=deque([])
    #print A
    for query in allquerys:
        L,R = query
        if curL == 0 and curR ==0:
            curL = L
            curR = L+1
            A = deque([dfsord[curL]])
        while curL< L:
            tp = dfsord[curL]
            if len(A) == 0 or tp !=A[0]:
                A.appendleft(tp)
            else:
                A.popleft()
            curL = curL +1
        while curL > L:
            tp = dfsord[curL-1]
            if len(A)!= 0 and  tp == A[0]:
                A.popleft()
            else:
                A.appendleft(tp)
            curL = curL -1
        while curR < R:
            tp = dfsord[curR]
            if len(A)!=0 and tp == A[-1]:
                A.pop()
            else:
                A.append(tp)
            curR = curR +1
            #print curR,A
        while curR > R:
            tp = dfsord[curR-1]
            if len(A)==0 or tp != A[-1]:
                A.append(tp)
            else:
                A.pop()
            curR = curR -1
        dic1[(L,R)] =list(A)
        #print L,R,A
    return dic1






def skippingSubpathSum(n, c, graph, queries):
    global querdic,mmpath
    answers = []
    for u,v in queries:
        querdic[(u,v)] =1
    queryPaths = []
    for u, v in queries:
        path = []
        dfs(graph, u, -1, v, path)
        queryPaths.append(path)
    allquerys = []
    for q1 in queryPaths:
        for q2 in q1:
            allquerys.append(q2)
    allquerys1= sorted(allquerys,cmp=rangeCompare)
    #print allquerys1
    dic1 =getAllRanges(allquerys1)
    for query in queryPaths:
        path=[]
        for q1 in query:
            pt = dic1[(q1[0],q1[1])]
            path.extend(pt)
        re =[]

        #print query,path
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
    
