class Solution(object):
    def maxBuilding(self, n, restrictions):
        rest =restrictions
        rest.append([1,0])
        rest.append([n,n-1])
        rest.sort()
        m =len(rest)
        for i in range(1,m):
            rest[i][1] = min( rest[i][1],rest[i-1][1] + rest[i][0]-rest[i-1][0] )
        for i in range(m-2,-1,-1):
            rest[i][1] = min(rest[i][1],rest[i+1][1] + rest[i+1][0] - rest[i][0])
        res =0
        for i in range(1,m):
            res = max(res,(rest[i][0]-rest[i-1][0] + rest[i][1] + rest[i-1][1])//2)
        return res