# Compare function
from functools import cmp_to_key
def compare(a,b):
    if (a+b)==(b+a):return 0
    return 1 if  (a+b)>(b+a) else -1

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    print(ls)
    return "".join(ls)


ls = ["8","81","82","829"]
print(sortArr(ls))