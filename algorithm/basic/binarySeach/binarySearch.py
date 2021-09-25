#file:///C:/books/1program/%E7%AE%97%E6%B3%95%E7%AB%9E%E8%B5%9B%E8%BF%9B%E9%98%B6%E6%8C%87%E5%8D%97.pdf  p36

def findX(l,r,x,a):
    while(l< r):
        mid = (l+r) >>1
        if(a[mid] >= x):
            r= mid
        else:
            l = mid +1
    return a[l]

def findX2(l,r,x,a):
    while l <r:
        mid = (1+r +1)>>1
        if a[mid] <=x :
            l = mid
        else:
            r = mid -1
    return a[l]

