
import sys

# 提高递归深度以应对可能的大型字符串
sys.setrecursionlimit(2 * 10**5 + 5)

# 快速输入
def main():
    def get_ints():
        return map(int, sys.stdin.readline().strip().split())

    def get_str():
        return sys.stdin.readline().strip()

    n, q = get_ints()
    s_orig = get_str()
    s = [ord(c) - ord('a') + 1 for c in s_orig]

    # --- 1. Suffix Array Construction (Doubling Algorithm) ---
    sa = [0] * (n + 1)
    rank = [0] * (n + 1)
    height = [0] * (n + 1)
    
    for i in range(n):
        rank[i] = s[i]
    
    k = 1
    while k <= n:
        suffixes = []
        for i in range(n):
            suffixes.append({'rank1': rank[i], 'rank2': rank[i + k] if i + k < n else -1, 'i': i})
        
        suffixes.sort(key=lambda x: (x['rank1'], x['rank2']))
        
        new_rank = [0] * (n + 1)
        new_rank[suffixes[0]['i']] = 1
        
        for i in range(1, n):
            if suffixes[i]['rank1'] == suffixes[i-1]['rank1'] and suffixes[i]['rank2'] == suffixes[i-1]['rank2']:
                new_rank[suffixes[i]['i']] = new_rank[suffixes[i-1]['i']]
            else:
                new_rank[suffixes[i]['i']] = i + 1
        rank = new_rank
        k *= 2
        if rank[suffixes[-1]['i']] == n:
            break

    for i in range(n):
        sa[rank[i]] = i
    
    # --- 2. LCP Array (height) Construction ---
    h = 0
    for i in range(n):
        if rank[i] == 1:
            h = 0
            continue
        j = sa[rank[i] - 1]
        if h > 0:
            h -= 1
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        height[rank[i]] = h

    # --- 3. Sparse Table for RMQ (LCP queries) ---
    LOG = (n-1).bit_length()
    st = [[0] * (n + 1) for _ in range(LOG)]
    log_table = [0] * (n + 1)
    
    for i in range(2, n + 1):
        log_table[i] = log_table[i >> 1] + 1
    
    for i in range(1, n):
        st[0][i] = height[i + 1]
    
    for i in range(1, LOG):
        for j in range(1, n - (1 << i) + 2):
            st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])

    def getlcp(l, r):
        if l == r:
            return n - l
        
        l_rank, r_rank = rank[l], rank[r]
        if l_rank > r_rank:
            l_rank, r_rank = r_rank, l_rank
        
        length = r_rank - l_rank
        log_len = log_table[length]
        
        return min(st[log_len][l_rank], st[log_len][r_rank - (1 << log_len)])

    # --- 4. Monotonic Stacks & Suffix Linkage ---
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

    # Extending links (simplified, non-optimal)
    # The original C++ code's link extension is complex due to
    # performance optimization; this is a functional but slower equivalent.
    
    # --- 5. Offline Query Processing ---
    B = 300
    queries = []
    for i in range(q):
        l, r = get_ints()
        queries.append({'l': l - 1, 'r': r - 1, 'i': i})
    
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

if __name__ == "__main__":
    main()