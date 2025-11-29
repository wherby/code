

def sosM(m):
    u = 1<<m 
    g = [[] for _ in range(1<<m)]
    for i in range(m):
        j = 0 
        bit = 1<<i
        while j < u:
            j |= bit 
            g[j].append(j^bit)
            j+=1
    return g 


g = sosM(6)
print(g)