
from collections import Counter
def resolve():
    N,M = list(map(lambda x: int(x),input().split()))
    AN =list(map(lambda x: int(x),input().split()))
    BN = list(map(lambda x: int(x),input().split()))
    #print(AN,BN)
    BN.sort(reverse=True)
    ca = Counter(AN)
    ks = list(ca.keys())
    ks.sort(reverse= True)

    #print(ks,[ca[k1] for k1 in ks])
    def verify(md):
        kv = ks[:md]
        ak = sum([ca[k1] for k1 in kv])
        nb = 0 
        for i,k in enumerate(kv):
            nb += ca[k]* (md -i)
        hb = sum(BN)
        #print(hb,BN)
        #print("a11",[ca[k1] for k1 in kv])
        res = 0
        cur = ak
        for i,b in enumerate(BN[:md]):
            if b >= cur:
                hb -= (b-cur)
            else:
                cur += cur -b 
            cur = cur - ca[kv[md-1-i]]
        #print(hb,nb,md,ak,sum(BN))
        return hb>=nb

    l,r = 0, min(M,len(ks))
    while l <r:
        md = (l+r+1)>>1
        if verify(md):
            l=md 
        else:
            r = md-1
    return sum([ca[k1] for k1 in ks[:l]])

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)