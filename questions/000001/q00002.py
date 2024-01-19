

# a/b
def divnum(a,b):
    n = len(bin(a)[2:])
    ret = [0]*n 
    res = a 
    for i in range(n):
        if ( (b <<(n-1-i)) <=res):
            ret[i] = 1 
            res = res - (b <<(n-1-i))
    return sum( a<<(n-1-i) for i,a in enumerate(ret))

print(divnum(10,3))
print(divnum(199,13))