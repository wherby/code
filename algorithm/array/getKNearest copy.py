
ls = [0,2,4,7,9,10]

def getKNearst(ls,k):
    ret = 10**30
    ls.sort()
    n = len(ls)
    pls = [0]
    for a in ls:
        pls.append(pls[-1] +a)
    for i in range(k-1,n):
        left = i-k+1 
        mid = (i+left)>>1
        acc = pls[i+1] - pls[mid+1] -ls[mid] * (i-mid)
        acc += ls[mid]*(mid-left+1) -(pls[mid+1] - pls[left])
        ret = min(ret,acc)
    return acc

print(getKNearst(ls,5))