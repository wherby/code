class Solution(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        inOrd =[0]*n
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            inOrd[a] +=1
            inOrd[b] +=1
        root = -1
        for i in range(n):
            if inOrd[i] ==1:
                root = i
                break
        allSM = sum(nums)
        ret = 0 
        def dfs(node,mid):
            if visit[node] == 1:
                return 0
            visit[node] = 1
            acc = 0
            #print(visit,node)
            for a in g[node]:
                if visit[a]==0:
                    #print("visit from", node,a ,acc)
                    re = dfs(a,mid)
                    
                    if re > mid:
                        return re
                    elif re == mid:
                        re =0
                    acc +=re
                    
            #print(acc,node,"aa")
            acc += nums[node]
            if acc ==mid:
                acc =0
            #print(acc,mid,node,visit, nums[node])
            return acc
        #print(root)
        for i in range(n,0,-1):
            if allSM % i == 0:
                mid = allSM //i
                visit =[0]*n
                re = dfs(root,mid)
                #print(re,i,mid)
                if re == 0:
                    ret = max(ret,i-1)
        return ret
                





re =Solution().componentValue([1,1,2,1,1],[[0,2],[1,2],[3,2],[4,2]] )
print(re)

## 0 1  2 3 4
## 1 1  2 1 1