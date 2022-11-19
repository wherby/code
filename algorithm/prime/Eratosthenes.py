# O(NloglogN) 效率接近线筛
def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

re =get_prime(1000000)
print(re[:10])
print(len(re))