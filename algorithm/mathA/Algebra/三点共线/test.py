

def sameLine(a,b,c):
    return (a[0] - b[0]) *(a[1]-c[1]) == (a[1] - b[1]) * (a[0] -c[0])

a= [0,0]
b = [1,1]
c = [2,2]
d = [-1,1]
e = [1,-1]
f = [1,2]
g = [-1,-1]

print(sameLine(a,b,g))
print(sameLine(a,b,c))
print(sameLine(a,b,d))
print(sameLine(a,d,e))
