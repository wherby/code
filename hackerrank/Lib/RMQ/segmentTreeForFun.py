import math
#https://docs.python.org/2/library/functools.html


MIN =  float("inf") *-1

def FN(fn):
    def newFun(a,b):
        return fn(a,b)
    return newFun

FNMAX = FN(max)




def RMQUtil(st, ss,se, qs,qe, index):
    global MIN
    if qs <= ss and qe >= se:
        return st[index]

    if se < qs or ss >qe:
        return MIN

    mid = (ss + se )/2
    return FNMAX(RMQUtil(st,ss,mid,qs,qe,2*index +1),
        RMQUtil(st,mid+1,se,qs,qe,2*index+2))


def RMQ(st,n, qs,qe):
    if qs < 0 or qe > n-1 or qs >qe:
        print "Invalid Input"
        return -1
    return RMQUtil(st,0,n-1,qs,qe,0)



def constructSTUtil(arr,start,end,st,si):
    if start == end:
        st[si] = arr[start]
        return arr[start]
    mid = (start + end) /2
    st[si] = FNMAX(constructSTUtil(arr,start,mid,st,si*2+1),
        constructSTUtil(arr,mid+1,end,st,si*2+2))
    return st[si]


def constructST(arr):
    n = len(arr)
    heigth = int(math.ceil(math.log(n,2)))
    max_size  = 2**heigth *2 -1
    st = [""]*max_size
    constructSTUtil(arr,0,n-1,st,0)
    return st 

if __name__ == "__main__":
    import random
    arr = [random.randint(0,10000) for i in range(100)]
    print arr
    st = constructST(arr)
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if RMQ(st,n,i,j) == max(arr[i:j+1]) :
                pass
            else:
                print "Not Equal for :"
                print i,j,arr