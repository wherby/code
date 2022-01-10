# 回溯法求所有组合值小于某具体值

ls = [1,2,3,4,5,6,7]
res =[]
n = len(ls)
limit =10
def dfs(idx,tls,sm):
    res.append(list(tls))
    if idx ==n:
        return
    for i in range(idx,n):
        if  ls[i]+ sm <=limit:
            print(i,idx,tls)
            tls.append(ls[i])
            dfs(i +1,tls,sm + ls[i])
            tls.pop()
    

dfs(0,[],0)
print(res)
print(len(res))
    
