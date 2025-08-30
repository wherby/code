# https://www.hackerrank.com/contests/w27/challenges/how-many-substrings/submissions/code/1396627128
# Fixed version
import functools
# rank[i] 表示 第i个字符开始的后缀子串 的排序index
# sa[i] 表示 第i个index对应的起始位置

def sa_fun(s_orig):
    n = len(s_orig)
    s = [ord(c) - ord('a') + 1 for c in s_orig]

    # --- 1. Suffix Array Construction (Doubling Algorithm) ---
    sa = [0] * n
    rank = [0] * n
    
    for i in range(n):
        rank[i] = s[i]
    
    k = 1
    while k < n:
        suffixes = []
        for i in range(n):
            suffixes.append({'rank1': rank[i], 'rank2': rank[i + k] if i + k < n else 0, 'i': i})
        
        suffixes.sort(key=lambda x: (x['rank1'], x['rank2']))
        
        new_rank = [0] * n
        idxN = 0 
        new_rank[suffixes[0]['i']] = idxN
        
        for i in range(1, n):
            if suffixes[i]['rank1'] == suffixes[i-1]['rank1'] and suffixes[i]['rank2'] == suffixes[i-1]['rank2']:
                new_rank[suffixes[i]['i']] = new_rank[suffixes[i-1]['i']]
            else:
                idxN +=1
                new_rank[suffixes[i]['i']] = idxN
        rank = new_rank
        k *= 2
        if idxN  ==n-1 :
            break

    for i in range(n):
        sa[rank[i]] = i
    return sa,rank

def lcp_sa(sa,rank,s):
    n = len(sa)
    height = [0]*n
    h = 0 

    for i in range(n):
        if rank[i] == 0:
            h = 0
            continue
        j = sa[rank[i] - 1]
        if h > 0:
            h -= 1
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        height[rank[i]] = h

    LOG = (n-1).bit_length()
    st = [[0] * n for _ in range(LOG)]
    log_table = [0] * n
    
    for i in range(2, n ):
        log_table[i] = log_table[i >> 1] + 1
    
    for i in range(n-1):
        # 因为 height[i]记录的是index是 i 与 i+1 的lcp
        st[0][i] = height[i + 1]
    
    for i in range(1, LOG):
        for j in range(0, n - (1 << i) ):
            st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
    
    return height,log_table,st

def getlcpWrap(n,log_table,st,rank):
    return functools.partial(getlcp_fun,n=n,log_table=log_table,st=st, rank =rank)

def getlcp_fun(l,r,n,log_table,st,rank):
    if l == r:
            return n - l
        
    l_rank, r_rank = rank[l], rank[r]
    if l_rank > r_rank:
        l_rank, r_rank = r_rank, l_rank
    
    length = r_rank - l_rank
    log_len = log_table[length]
    
    return min(st[log_len][l_rank], st[log_len][r_rank- (1 << log_len)])

def getSeqLink(n, rank):
    """
    这个函数是 C++ 代码的 Python 0-indexed 版本。
    它根据后缀的 rank 值构建一个层级链接结构。
    """
    # 
    # 初始化一个列表的列表，用于存储链接。
    # seq[i][0] 存储 rank 值比 rank[i] 小的链接
    # seq[i][1] 存储 rank 值比 rank[i] 大的链接
    seq = [[[] for _ in range(2)] for _ in range(n)]

    # --- 对应 C++ 的第一个代码块 ---
    # 这部分使用单调栈来为每个后缀 i 找到其左侧第一个 rank 值比它小 (seq[i][0])
    # 和第一个 rank 值比它大 (seq[i][1]) 的后缀。
    
    # 寻找左侧第一个 rank 更小的后缀
    # 使用 Python 的列表作为栈
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] < rank[i]:
            stack.pop()
        if stack:
            seq[i][0].append(stack[-1])
        stack.append(i)
    
    # 寻找左侧第一个 rank 更大的后缀
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and rank[stack[-1]] > rank[i]:
            stack.pop()
        if stack:
            seq[i][1].append(stack[-1])
        stack.append(i)
    
    # --- 对应 C++ 的第二个代码块 ---
    # 这部分扩展上面找到的初始链接，形成更长的“跳转”链条。
    # Python 的二分查找逻辑等效于 C++ 中带有自定义比较函数 (cmp1, cmp2) 的 lower_bound。
    for i in range(n - 1, -1, -1):
        # 扩展 rank 更小的链接链条
        if seq[i][0]:
            node = seq[i][0][0]
            while True:
                # 在 node 的“更大”链接中，用二分查找找到第一个 rank >= rank[i] 的跳转点
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

        # 扩展 rank 更大的链接链条
        if seq[i][1]:
            node = seq[i][1][0]
            while True:
                # 在 node 的“更小”链接中，用二分查找找到第一个 rank <= rank[i] 的跳转点
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
            for j in range(1, n+1 ):
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
    # for i in range(len(s1)):
    #     print(s1[sa[i]:])
    # height2 =[]
    # for i in range(1,len(s1)):
    #     xi = sa[i-1]
    #     xj = sa[i]
    #     height2.append(smplcp(s1[xi:],s1[xj:]))
    # height2 =[0] +height2
    # print(height2)
    # print(height == height2)
    print("-==== lcp ====")
    for i in range(len(s1)):
        for j in range(i):
            if getlcp_fun(i,j,len(s1),log_table,st,rank) != smplcp(s1[i:],s1[j:]):
                print(i,j, getlcp_fun(i,j,len(s1),log_table,st,rank),smplcp(s1[i:],s1[j:]))
    print("-==== seq link ====")
    seq = getSeqLink(len(s1),rank)
    #print(seq)
    qrs = [(61,97),(15,50),(41,78),(7,36)]
    getlcp = getlcpWrap(len(s1),log_table,st,rank)
    offlineQuery(qrs,len(s1),seq,getlcp)