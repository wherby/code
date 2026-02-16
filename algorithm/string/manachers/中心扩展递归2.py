def get_max_len(s, k):
    n = len(s)
    if k >= n: return n
    ans = 0

    # 处理 2n-1 个中心点
    for i in range(2 * n - 1):
        l, r = i // 2, (i + 1) // 2
        
        # current_k: 当前已消耗的跳过机会
        # window_l, window_r: 记录当前探索到的最远边界
        # 我们用一个简单的局部搜索，因为 k 通常比较小
        
        # 初始扩展：跳过所有匹配的
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        
        # 此时 s[l] != s[r]，开始处理 k
        # 使用 BFS 思想探索所有可能的跳过组合，但限制深度为 k
        # queue 存储 (当前左边界, 当前右边界, 剩余k)
        queue = [(l, r, k)]
        visited = set()
        
        while queue:
            curr_l, curr_r, curr_k = queue.pop(0)
            
            # 更新全局最大长度：区间是 (curr_l, curr_r)，不含边界
            ans = max(ans, curr_r - curr_l - 1)
            if ans == n: return n # 终极剪枝
            
            if curr_k > 0:
                # 尝试跳过左边
                next_l, next_r = curr_l - 1, curr_r
                if next_l >= -1:
                    # 扩展跳过后的匹配字符
                    while next_l >= 0 and next_r < n and s[next_l] == s[next_r]:
                        next_l -= 1
                        next_r += 1
                    state = (next_l, next_r, curr_k - 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
                
                # 尝试跳过右边
                next_l, next_r = curr_l, curr_r + 1
                if next_r <= n:
                    # 扩展跳过后的匹配字符
                    while next_l >= 0 and next_r < n and s[next_l] == s[next_r]:
                        next_l -= 1
                        next_r += 1
                    state = (next_l, next_r, curr_k - 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
                        
    return ans