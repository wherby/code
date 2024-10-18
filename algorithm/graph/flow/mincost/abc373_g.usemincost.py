# Will TLE
# https://atcoder.jp/contests/abc373/submissions/58854744
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin






# Python3 program to implement
# the above approach
from sys import maxsize
from typing import List
 
# Stores the found edges
found = []
 
# Stores the number of nodes
N = 0
 
# Stores the capacity
# of each edge
cap = []
 
flow = []
 
# Stores the cost per
# unit flow of each edge
cost = []
 
# Stores the distance from each node
# and picked edges for each node
dad = []
dist = []
pi = []
 
INF = maxsize // 2 - 1
 
# Function to check if it is possible to
# have a flow from the src to sink
def search(src: int, sink: int) -> bool:

    # Initialise found[] to false
    found = [False for _ in range(N)]
 
    # Initialise the dist[] to INF
    dist = [INF for _ in range(N + 1)]
 
    # Distance from the source node
    dist[src] = 0
 
    # Iterate until src reaches N
    while (src != N):
        best = N
        found[src] = True
 
        for k in range(N):
 
            # If already found
            if (found[k]):
                continue
 
            # Evaluate while flow
            # is still in supply
            if (flow[k][src] != 0):
 
                # Obtain the total value
                val = (dist[src] + pi[src] -
                           pi[k] - cost[k][src])
 
                # If dist[k] is > minimum value
                if (dist[k] > val):
 
                    # Update
                    dist[k] = val
                    dad[k] = src
 
            if (flow[src][k] < cap[src][k]):
                val = (dist[src] + pi[src] -
                           pi[k] + cost[src][k])
 
                # If dist[k] is > minimum value
                if (dist[k] > val):
 
                    # Update
                    dist[k] = val
                    dad[k] = src
 
            if (dist[k] < dist[best]):
                best = k
 
        # Update src to best for
        # next iteration
        src = best
 
    for k in range(N):
        pi[k] = min(pi[k] + dist[k], INF)
 
    # Return the value obtained at sink
    return found[sink]
 
# Function to obtain the maximum Flow
def getMaxFlow(capi: List[List[int]], 
              costi: List[List[int]], 
              src: int, sink: int) -> List[int]:
 
    global cap, cost, found, dist, pi, N, flow, dad
    cap = capi
    cost = costi
 
    N = len(capi)
    found = [False for _ in range(N)]
    flow = [[0 for _ in range(N)]
               for _ in range(N)]
    dist = [INF for _ in range(N + 1)]
    dad = [0 for _ in range(N)]
    pi = [0 for _ in range(N)]
 
    totflow = 0
    totcost = 0
 
    # If a path exist from src to sink
    while (search(src, sink)):
 
        # Set the default amount
        amt = INF
        x = sink
         
        while x != src:
            amt = min(
                amt, flow[x][dad[x]] if
                (flow[x][dad[x]] != 0) else
                  cap[dad[x]][x] - flow[dad[x]][x])
            x = dad[x]
 
        x = sink
         
        while x != src:
            if (flow[x][dad[x]] != 0):
                flow[x][dad[x]] -= amt
                totcost -= amt * cost[x][dad[x]]
 
            else:
                flow[dad[x]][x] += amt
                totcost += amt * cost[dad[x]][x]
                 
            x = dad[x]
 
        totflow += amt
 
    # Return pair total cost and sink
    return [totflow, totcost]
 

n = int(input())
als,bls= [],[]
for _ in range(n):
    als.append(list(map(lambda x: int(x),input().split())))
for _ in range(n):
    bls.append(list(map(lambda x: int(x),input().split())))

s = n*2
t = 2*n+1
cap = [[0]*(n*2+2) for _ in range(n*2+2)]
cost = [[0]*(n*2+2) for _ in range(n*2+2)]
C = 1.5*(10**13)


for i in range(n):
    cap[s][i] =1
    cap[i+n][t] =1
    for j in range(n):
        x1 = ( (als[i][0] - bls[j][0]) **2 + (als[i][1]-bls[j][1])**2)**(1/2) 
        cap[i][j+n] =1
        cost[i][j+n] = C*x1 +0.5
        cost[j+n][i] = -(C*x1 +0.5)
f,c = getMaxFlow(cap,cost,s,t)
ret = [0]*n
for i in range(n):
    for j in range(n):
        if flow[i][j+n] ==1:
            ret[i] = j+1

print(" ".join([str(a) for a in ret]))  

