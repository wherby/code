from bisect import bisect_right,insort_left,bisect_left
ls = [0,2,4,7,9,10]
n = len(ls)
pls = [0]
for a in ls:
    pls.append(pls[-1] +a )

# k not include i self
def getK(i,k):
    l,r = 0,ls[-1]
    while l <r:
        mid =(l+r)>>1
        left = bisect_left(ls,ls[i]-mid)
        right = bisect_right(ls,ls[i]+mid)
        if right-left-1 <k:
            l= mid+1
        else:
            r = mid
    left = bisect_left(ls,ls[i]-l)
    right = bisect_right(ls,ls[i]+l)
    if right-left-1  <k:
        return 10**20
    acc =0
    acc += pls[right]- pls[i+1] - ls[i] *(right-i-1)
    acc +=  ls[i]*(i-left+1)- (pls[i+1] -pls[left])
    return acc 

print(ls)
for i in range(n):
    print(getK(i,4), i)