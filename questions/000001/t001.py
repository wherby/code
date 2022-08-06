
def getCnt(x):
    acc =0
    cnt = 0
    while acc <100 and x >0:
        acc += x 
        cnt +=1
        x-=1
    return cnt if x>0 else 100

def getAns():
    l,r =0,100
    while l <r :
        mid = (l+r)>>1
        if getCnt(mid) > mid:
            l = mid +1
        else:
            r = mid
    return l
re =getAns()
print(re)
