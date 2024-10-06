from collections import defaultdict,deque
def getSubListUnderN(n):
    dic =defaultdict(set)
    visited=[[] for _ in range(n+2)]
    dic[1] = set([1])
    for i in range(2,n+1):
        if len(visited[i]):
            a = visited[i][0]
            k = i // a
            s =set(dic[k])
            t =set(s)
            for b in s:
                t.add(b*a) 
            dic[i] = t
            continue
        dic[i]=set([1,i])
        for j in range(i,n+1,i):
            visited[j].append(i)
    return dic

d = getSubListUnderN(100000)
print(d[100])
print(d[102])
    