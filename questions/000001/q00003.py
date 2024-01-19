

# a/b 
# m : 二进制小数位数
def divnum(a,b,m=100):
    n = len(bin(a)[2:]) +m
    ret = [0]*n
    res = a <<m
    for i in range(n):
        if ( (b <<(n-1-i)) <=res):
            ret[i] = 1 
            res = res - (b <<(n-1-i))
    return sum( float(a<<(n-1-i))/(1<<m) for i,a in enumerate(ret))

print(divnum(10,3))
print(divnum(199,13))