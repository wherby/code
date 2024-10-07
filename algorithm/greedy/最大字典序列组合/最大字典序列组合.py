from functools import cmp_to_key
def compare(a,b):
    return int(a+b) -int(b+a)

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    print(ls)
    return "".join(ls)


ls = ["8","81","82","829"]
print(sortArr(ls))