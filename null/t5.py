#B->A
#D->B
#D->C
#C->A
#E->C

def dfs(g,cand,child,dp):
    res =[]
    if len(g[cand]) == 0:
        return [cand]
    for i in g[cand]:
        re = dfs(g,i,[],dp)
        res = res + re
    res.append(cand)
    for i in res:
        #print("cc",dp,i,cand,res)
        dp[cand][i] =1
    #print(res,cand)
    return res



def findRelation(ls,n):
    dp=[{} for i in range(n)]
    lss =[0] *n
    g =[[] for i in range(n)]
    for t in ls:
        a,b = t[0],t[1]
        lss[b] +=1
        g[a].append(b)
    #print(g,lss)
    
    for i,v in enumerate(lss):
        #print("a ", i,v)
        if v == 0 :
            dfs(g,i,[],dp)
    print(dp)


    

ls = [[1,0],[3,1],[3,2],[2,0],[4,2]]
findRelation(ls,5)
