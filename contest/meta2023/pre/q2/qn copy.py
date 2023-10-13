a,b,c = 0,0,0
def findX(mid):
    global a,b,c
    if mid <0 or (c-mid*a)<0:
        return 0
    
    x,y = mid,(c-mid*a)//b
    #print("x",x,y)
    return x+ 2*y-(x==0 and y >0)

def resolve():
    global a,b,c
    isG = True
    a,b,c = list(map(lambda x: int(x),input().split()))
    #print(a,b,c)
    l,r = 0,c//a 
    #print(l,r,c,a)
    while l<r-1:
        mid = (l+r)//2
        mmid = (mid+r)//2
        if findX(mid) > findX(mmid):
            r = mmid
        else:
            l =mid 
        # if a ==5:
        #print("X",l,r)
    #print(l,r)
    mx = 0 
    for i in range(-10000,10000):
        mx =max(mx,findX(l+i))
    return mx
    

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)