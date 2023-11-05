class Solution:
    def smallestMissingValueSubtree(self, parents, nums) :
        n = len(parents)
        tree = []
        indx1 = -1
        for i in range(n):
            tree.append([])
        for i in range(n):
            p = parents[i]
            if p != -1:
                tree[p].append(i)
        for i in range(n):
            if nums[i] == 1:
                indx1 =i
        if indx1 ==-1:
            return [1] * n
        res = [1] *n
        idx =indx1
        seqv =[]
        while idx != -1:
            res[idx] = 1000000
            seqv.append(idx)
            idx = parents[idx]
        msk = [0] *100010
        missIndex =1
        visted = [0] * 10010
        def searchLastes():
            while msk[missIndex] == 1 :
                missIndex +=1
            return missIndex
        def dfs(x):
            child = tree[x]
            for c in child :
                if visted[c] ==0:
                    dfs(c)
            msk[nums[x]] =1
            #print(msk[:10])
            #print(x,res[x])
            visted[x] = 1
            if res[x] == 1000000:
                indx = searchLastes()
                res[x]=indx
                return indx
        for v in seqv:
            dfs(v)
        return res
        


parents = [-1,0,1,0,3,3]
nums = [5,4,6,2,1,3]
re = Solution().smallestMissingValueSubtree(parents,nums)
print(re)