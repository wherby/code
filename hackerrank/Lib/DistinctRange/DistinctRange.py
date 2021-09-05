# For input array ls, find max any distinct range [a,b] don't contains same element.

def getDistRange(ls):
    n = len(ls)
    vis =[0] *n
    mx = [0] *n
    po =0
    d = ls
    for i in range(n):
        while po< n and vis[d[po]] == 0:
            vis[d[po]] =1 +vis[d[po]]
            po =po+1
        mx[i] = po
        vis[d[i]] =vis[d[i]]-1
    print mx
    return mx



ls =[6, 5,5, 1, 2, 4, 6, 1]
getDistRange(ls)