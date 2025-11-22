

from collections import defaultdict,deque
def resolve():
    isG = False
    N,K,M = list(map(lambda x: int(x),input().split()))
    routes = []
    occurrences = [[] for _ in range(N + 1)]
    for i in range(M):
        t1 = list(map(lambda x: int(x),input().split()))
        for j,a in enumerate(t1[1:]):
            occurrences[a].append((i,j))
        routes.append(t1[1:])
    dist = [-1] * (N + 1)
    dist[1] = 0

    current_level = [1]
    level = 1 
    
    expanded = [set() for _ in range(M)]

    while current_level:
        route_positions = [[] for _ in range(M)]
        
        for u in current_level:
            for rid, pos in occurrences[u]:
                route_positions[rid].append(pos)
        
        next_level_set = set()
        
        for rid in range(M):
            if not route_positions[rid]:
                continue
                
            route = routes[rid]
            L = len(route)
            
            ranges = []
            for pos in route_positions[rid]:
                start = pos + 1
                end = min(pos + K, L - 1)
                if start <= end:
                    ranges.append((start, end))
            
            if not ranges:
                continue
            
            ranges.sort()
            merged = []
            current_start, current_end = ranges[0]
            for start, end in ranges[1:]:
                if start <= current_end + 1:
                    current_end = max(current_end, end)
                else:
                    merged.append((current_start, current_end))
                    current_start, current_end = start, end
            merged.append((current_start, current_end))
            
            for start, end in merged:
                for j in range(start, end + 1):
                    if j not in expanded[rid]:
                        expanded[rid].add(j)
                        v = route[j]
                        if dist[v] == -1:
                            dist[v] = level
                            next_level_set.add(v)
        
        current_level = list(next_level_set)
        level += 1

    total = 0
    for i in range(1, N + 1):
        total += dist[i] * i
    return total

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)