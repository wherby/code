# lee215

class Solution:
    def minimumCost(self, cost: list[int], roads: list[list[int]]) -> int:
        n = len(cost)
        G = [[] for i in range(n)]
        for i,j in roads:
            G[i].append(j)
            G[j].append(i)
        low = [n] * n
        seen = {}
        cut = [0] * n
        inf = float('inf')
        res = []

        def tarjan(i):
            seen[i] = len(seen) + 1
            children = 0
            min_cost = inf
            count_cut = 0
            for j in G[i]:
                if j in seen:
                    low[i] = min(low[i], seen[j])
                    continue
                children += 1
                cur_cost, cur_cut = tarjan(j)
                low[i] = min(low[i], low[j])
                if seen[i] <= low[j]:
                    cut[i] += i != root or children > 1
                    if cur_cut < 1:
                        res.append(cur_cost)
                else:
                    min_cost = min(min_cost, cur_cost)
                    count_cut += cur_cut
            if cut[i]:
                count_cut += 1
            else:
                min_cost = min(min_cost, cost[i])
                
            if i == root:
                if children == 1 and cur_cut < 1:
                    res.remove(cur_cost)
                min_cost = min(min_cost, cur_cost)
                count_cut += cur_cut
                if cut[i] == 0 and count_cut < 2:
                    res.append(min_cost)
                    return
            return [min_cost, count_cut]
        
        root = 0
        tarjan(root)
        print(res)
        return sum(res) - max(res) if len(res) > 1 else min(cost)
    
    
re = Solution().minimumCost(cost = [1,2,3,4],roads = [[0,1],[0,2],[0,3]])
#re = Solution().minimumCost(cost = [1,2,3,4,5,6],roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]])
print(re)