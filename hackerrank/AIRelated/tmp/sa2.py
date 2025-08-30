# Wrong getSeqLink
import functools
# rank[i] 表示 第i个字符开始的后缀子串 的排序index
# sa[i] 表示 第i个index对应的起始位置

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
    
def getSeqLink(n,rank):
    seq = [[[] for _ in range(2)] for _ in range(n)]
    # Stack for smaller rank to the left
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] < rank[i]:
            stack.pop()
        if stack:
            seq[i][0].append(stack[-1])
        stack.append(i)
    
    # Stack for larger rank to the left
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] > rank[i]:
            stack.pop()
        if stack:
            seq[i][1].append(stack[-1])
        stack.append(i)
    
    for i in range(n - 1, -1, -1):
        # Process links for smaller ranks
        if seq[i][0]:
            node = seq[i][0][0]
            while True:
                # Find the position to insert `i` into `seq[node][1]`
                # The original C++ code uses cmp1, which sorts by rank[u] < rank[v].
                # This is equivalent to finding the first element in seq[node][1] whose rank is >= rank[i].
                
                # Since seq[node][1] stores links to larger ranks, it is sorted by rank in descending order.
                # We need to find the first element whose rank is less than or equal to rank[i]
                # to extend the link. We'll use a manual binary search or a custom helper.
                
                # The C++ code's `lower_bound` with `cmp1` on a descendingly sorted list
                # is a bit non-standard and implies a specific search for the first
                # element whose rank is NOT less than `rank[i]`, i.e., `rank[node] >= rank[i]`.
                # Let's write a simple binary search equivalent to capture this logic.
                
                low, high = 0, len(seq[node][1]) - 1
                it = len(seq[node][1])
                while low <= high:
                    mid = (low + high) // 2
                    if rank[seq[node][1][mid]] < rank[i]:
                        high = mid - 1
                    else:
                        it = mid
                        low = mid + 1

                if it == len(seq[node][1]):
                    break
                else:
                    node = seq[node][1][it]
                    seq[i][0].append(node)

        # Process links for larger ranks
        if seq[i][1]:
            node = seq[i][1][0]
            while True:
                # The original C++ code uses `lower_bound` with `cmp2` on `seq[node][0]`.
                # `cmp2` sorts by rank descending. `seq[node][0]` is sorted by rank ascending.
                # `lower_bound` finds the first element not less than `i`.
                # The `cmp2` lambda reverses the comparison, so it effectively finds the first element
                # whose rank is not GREATER than `rank[i]`, i.e., `rank[node] <= rank[i]`.
                
                # `bisect.bisect_left` is perfect for this, but we need to pass a key function.
                # Unfortunately, `bisect` doesn't accept a key.
                # So, a custom binary search is the best way to translate this logic.
                
                low, high = 0, len(seq[node][0]) - 1
                it = len(seq[node][0])
                while low <= high:
                    mid = (low + high) // 2
                    if rank[seq[node][0][mid]] > rank[i]:
                        low = mid + 1
                    else:
                        it = mid
                        high = mid - 1
                
                if it == len(seq[node][0]):
                    break
                else:
                    node = seq[node][0][it]
                    seq[i][1].append(node)
    return seq

def offlineQuery(qrs,n,seq,getlcp):
    B = 300
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
            for j in range(1, n + 1):
                now += delta[j - 1]
                s_prefix[j] = s_prefix[j-1] + now
       # print(events,queries)
        while query_idx >= 0 and queries[query_idx]['l'] == i:
            current_query = queries[query_idx]
            query_ans = s_prefix[current_query['r'] + 1]
            for event in events:
                pos = event['pos']
                val = event['val']
                if pos <= current_query['r']:
                    query_ans += val * (current_query['r'] - pos + 1)
            ans[current_query['i']] = query_ans
            query_idx -= 1

    for i in range(q):
        print(ans[i])
    #print(s_prefix)

def smplcp(s1,s2):
    cnt = 0
    for a,b in zip(s1,s2):
        if a ==b:
            cnt +=1
        else:
            return cnt

if __name__ == '__main__':
    s1 = "qqqqqqqqqqzrzrrzrzrrzrrzrzrrzrzrrzttttttttttttttttttttttttttttttttttttttttttttttttttttttqncpqzcxpbwa"
    print(sa_fun(s1))
    sa,rank= sa_fun(s1)
    for i in range(len(s1)):
        print(i,sa[rank[i]])
    height,log_table,st = lcp_sa(sa,rank,s1)
    print("-==== height ====")
    print(height)
    for i in range(len(s1)):
        print(s1[sa[i]:])
    height2 =[]
    for i in range(1,len(s1)):
        xi = sa[i-1]
        xj = sa[i]
        height2.append(smplcp(s1[xi:],s1[xj:]))
    height2 =[0] +height2
    print(height2)
    print(height == height2)
    print("-==== lcp ====")
    for i in range(len(s1)):
        for j in range(i):
            if getlcp_fun(i,j,len(s1),log_table,st,rank) != smplcp(s1[i:],s1[j:]):
                print(i,j, getlcp_fun(i,j,len(s1),log_table,st,rank),smplcp(s1[i:],s1[j:]))
    print("-==== seq link ====")
    seq = getSeqLink(len(s1),rank)
    #print(seq)
    qrs = [(61,97),(15,50)]
    getlcp = getlcpWrap(len(s1),log_table,st,rank)
    offlineQuery(qrs,len(s1),seq,getlcp)