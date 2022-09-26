import random
def floyd_sampler(n, k):
    H = set()
    for i in range(n-k, n):
        r = random.randint(0,i+1)
        if r in H:
            yield i
            H.add(i)
        else:
            yield r
            H.add(r)
    return H
            
re = floyd_sampler(11,10)
print(list(re))