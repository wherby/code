a=[1,2,2,3,3,4,4,5,5]
b=[1,1,1]

def unify(a):
    b= [a[i] for i in range(0,len(a)) if i==0 or a[i-1] != a[i]]
    print(b)

unify(a)
unify(b)



