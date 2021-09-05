
a=[(1,2,3),(4,5,6),(7,8,9)]
print(zip(*a))
print(map(None,*a))
#print(map(max,*a))

f1 = lambda(a): [tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0]))]
print f1(a)

b = [(1,2,3),(4,5,6),(7,8,9),(10,11)]
print zip(*b)
#print f1(b)
print map(None,*b)

f2 = lambda(a): [tuple(a[j][i] for j in range(len(a))) for i in range(min(map(len,a)))]
print f2(b)
arg = a
print(zip(*arg))










