# https://www.hackerrank.com/contests/w27/challenges/how-many-substrings/submissions/code/1396627128


import sys,os
parent_directory_concise= os.path.dirname(os.path.abspath(__file__))
for i in range(0):
    parent_directory_concise = os.path.dirname(parent_directory_concise)
sys.path.append(parent_directory_concise)
print("init_setting and python path added...")

filename = parent_directory_concise+"/input/input2.txt"
f=open(filename,'r')
sys.stdin=f
import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_list =[]
        if args:
            arg_list.append( ", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{0} = {1}'.format(k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print('[{0}] :{1} ' .format( elapsed, name))
        return result
    return clocked



import math
import os
import random
import re
import sys
import functools

#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def sa_fun(s_orig):
    n = len(s_orig)
    s = [ord(c) - ord('a') + 1 for c in s_orig]

    # Initialize SA and rank arrays
    sa = list(range(n))
    rank = s.copy()  # Initial rank is the character values
    
    k = 1
    while k < n:
        # Create list of (rank1, rank2, index) tuples
        tuples = []
        for i in range(n):
            rank1 = rank[i]
            rank2 = rank[i + k] if i + k < n else 0
            tuples.append((rank1, rank2, i))
        
        # Sort by first rank, then second rank
        tuples.sort()
        
        # Reassign ranks
        new_rank = [0] * n
        current_rank = 0
        new_rank[tuples[0][2]] = current_rank
        
        for i in range(1, n):
            # If same ranks as previous, assign same rank number
            if tuples[i][0] == tuples[i-1][0] and tuples[i][1] == tuples[i-1][1]:
                new_rank[tuples[i][2]] = current_rank
            else:
                current_rank += 1
                new_rank[tuples[i][2]] = current_rank
        
        rank = new_rank
        
        # If all suffixes have unique ranks, we're done
        if current_rank == n - 1:
            break
            
        k *= 2
    
    # Build SA from rank array
    sa = [0] * n
    for i in range(n):
        sa[rank[i]] = i
    
    return sa, rank

def lcp_sa(sa, rank, s):
    n = len(sa)
    height = [0] * n
    
    # Kasai's algorithm for LCP array
    k = 0
    for i in range(n):
        if rank[i] == 0:
            k = 0
            continue
            
        j = sa[rank[i] - 1]  # Previous suffix in suffix array
        
        # Extend common prefix
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
            
        height[rank[i]] = k
        
        if k > 0:
            k -= 1  # Kasai's optimization

    # Build sparse table for range minimum queries
    LOG = (n).bit_length()  # Number of levels needed
    st = [[0] * n for _ in range(LOG)]
    
    # Precompute log table for efficient range queries
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1
    
    # Initialize base level of sparse table
    # height[i] contains LCP between SA[i] and SA[i+1]
    for i in range(n - 1):
        st[0][i] = height[i + 1]  # Correct: LCP between adjacent suffixes
    
    # Build sparse table
    for i in range(1, LOG):
        step = 1 << (i - 1)
        for j in range(n - (1 << i)):
            st[i][j] = min(st[i - 1][j], st[i - 1][j + step])
    
    return height, log_table, st

def getlcpWrap(n,log_table,st,rank):
    return functools.partial(getlcp_fun,n=n,log_table=log_table,st=st, rank =rank)

def getlcp_fun(l, r, n, log_table, st, rank):
    if l == r:
        return n - l  # Same position, LCP is remaining string length
    
    # Get ranks of the two suffixes
    l_rank, r_rank = rank[l], rank[r]
    #print(l,r,l_rank,r_rank,)
    # Ensure l_rank < r_rank
    if l_rank > r_rank:
        l_rank, r_rank = r_rank, l_rank

    

    query_start = l_rank
    query_end = r_rank 
    query_length = query_end - query_start 
    
    # Find the appropriate log level
    k = log_table[query_length]
    #print(query_start,query_end,k,st[k][query_start],st[k][query_end - (1 << k) ])
    # Query the sparse table - we want the minimum in range [query_start, query_end]
    # This is equivalent to min(st[k][query_start], st[k][query_end - (1 << k) + 1])
    return min(st[k][query_start], st[k][query_end - (1 << k) ])

def getSeqLink(n, rank):

    seq = [[[] for _ in range(2)] for _ in range(n)]

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] < rank[i]:
            stack.pop()
        if stack:
            seq[i][0].append(stack[-1])
        stack.append(i)
    
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] > rank[i]:
            stack.pop()
        if stack:
            seq[i][1].append(stack[-1])
        stack.append(i)
    for i in range(n - 1, -1, -1):
        if seq[i][0]:
            node = seq[i][0][0]
            while True:
                low, high = 0, len(seq[node][1]) - 1
                it = len(seq[node][1])
                while low <= high:
                    mid = (low + high) // 2
                    if rank[seq[node][1][mid]] >= rank[i]:
                        it = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                
                if it == len(seq[node][1]): 
                    break
                
                node = seq[node][1][it]
                seq[i][0].append(node)


        if seq[i][1]:
            node = seq[i][1][0]
            while True:
                low, high = 0, len(seq[node][0]) - 1
                it = len(seq[node][0])
                while low <= high:
                    mid = (low + high) // 2
                    if rank[seq[node][0][mid]] <= rank[i]:
                        it = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                
                if it == len(seq[node][0]): 
                    break
                
                node = seq[node][0][it]
                seq[i][1].append(node)
                
    return seq
@clock
def offlineQuery(qrs,n,seq,getlcp):
    B = 1000
    queries = []
    for i,(l,r) in enumerate(qrs):
        queries.append({'l': l , 'r': r , 'i': i})
    q= len(qrs)
    queries.sort(key=lambda x: x['l'])

    delta = [0] * (n + 1)
    s_prefix = [0] * (n + 1)
    lcp_cache = [0] * (n + 1)
    events = []
    
    ans = [0] * q
    query_idx = q - 1

    def update(x, length):
        if lcp_cache[x] < length:
            events.append({'pos': x + lcp_cache[x], 'val': -1})
            events.append({'pos': x + length, 'val': 1})
            lcp_cache[x] = length

    for i in range(n - 1, -1, -1):
        events.append({'pos': i, 'val': 1})
        for neighbor in seq[i][0]:
            update(neighbor, getlcp(i, neighbor))
        for neighbor in seq[i][1]:
            update(neighbor, getlcp(i, neighbor))
            
        if len(events) > B:
            for event in events:
                delta[event['pos']] += event['val']
            events = []
            
            now = 0
            for j in range(0, n ):
                now += delta[j]
                s_prefix[j] =now +s_prefix[j-1]
       # print(events,queries)
        while query_idx >= 0 and queries[query_idx]['l'] == i:
            current_query = queries[query_idx]
            query_ans = s_prefix[current_query['r'] ]
            for event in events:
                pos = event['pos']
                val = event['val']
                if pos <= current_query['r']:
                    query_ans += val * (current_query['r'] - pos + 1)
            ans[current_query['i']] = query_ans
            query_idx -= 1

    # for i in range(q):
    #     print(ans[i])
    return ans

def countSubstrings(s, queries):
    # Write your code here
    #print(s,queries)
    n = len(s)
    sa,rank= sa_fun(s)
    print("step1")
    height,log_table,st = lcp_sa(sa,rank,s)
    seq = getSeqLink(n,rank)
    print("step3")
    getlcp = getlcpWrap(n,log_table,st,rank)
    return offlineQuery(queries,n,seq,getlcp)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    s = input()

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = countSubstrings(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()