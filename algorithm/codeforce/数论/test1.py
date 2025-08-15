

def getOddC(g):
    g1=g//( g&(-g))
    print(g,g1)
    return g1

for g in range(1,32):
    print(g,getOddC(g),bin(g))