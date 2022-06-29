def arrDiff(ls):
    n = len(ls)
    res = [0]*n 
    res[0] = sum(ls) - n *ls[0]
    for i in range(1,n):
        res[i] = res[i-1] +(ls[i] -ls[i-1]) *i - (n-i) *(ls[i] -ls[i-1])
    return res

def arrDiff2(ls):
    n = len (ls)
    res =[0]*n
    pre  =[0]*(n+1)
    for i in range(n):
        pre[i+1] =pre[i] + ls[i]
    for i in range(n):
        res[i] = i*ls[i] - pre[i] + pre[n] - pre[i+1] -ls[i] * (n-i-1)
    return res


# 把队列的值变成对应下标数字所需要的cost
ls =[1,2,3,4,5,6,7,8]
res1 = arrDiff(ls)
print(res1)
res2 =arrDiff2(ls)
print(res2)