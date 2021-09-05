a=(1,2,3)
print(id(a))    

def test(a):
    print(id(a))
    b = tuple(list(a))
    print(id(b))

test(a)