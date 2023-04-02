# shortest-cycle-in-an-undirected-unweighted-graph

from sys import maxsize as INT_MAX
from collections import deque
 
N = 100200
 
gr = [0] * N
for i in range(N):
    gr[i] = []
 
# Function to add edge
def add_edge(x: int, y: int) -> None:
    global gr
    gr[x].append(y)
    gr[y].append(x)
 
# Function to find the length of
# the shortest cycle in the graph
def shortest_cycle(n: int) -> int:
 
    # To store length of the shortest cycle
    ans = INT_MAX
 
    # For all vertices
    for i in range(n):
 
        # Make distance maximum
        dist = [int(1e9)] * n
 
        # Take a imaginary parent
        par = [-1] * n
 
        # Distance of source to source is 0
        dist[i] = 0
        q = deque()
 
        # Push the source element
        q.append(i)
 
        # Continue until queue is not empty
        while q:
 
            # Take the first element
            x = q[0]
            q.popleft()
 
            # Traverse for all it's childs
            for child in gr[x]:
 
                # If it is not visited yet
                if dist[child] == int(1e9):
 
                    # Increase distance by 1
                    dist[child] = 1 + dist[x]
 
                    # Change parent
                    par[child] = x
 
                    # Push into the queue
                    q.append(child)
 
                # If it is already visited
                elif par[x] != child and par[child] != x:
                    ans = min(ans, dist[x] +
                                   dist[child] + 1)
 
    # If graph contains no cycle
    if ans == INT_MAX:
        return -1
 
    # If graph contains cycle
    else:
        return ans