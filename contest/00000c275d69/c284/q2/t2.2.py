class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        ans = 0
        s = set((x,y) for x,y in dig)
        for x1,y1,x2,y2 in artifacts:
            if all((x,y) in s for x in range(x1,x2+1) for y in range(y1,y2+1)):
                ans +=1
        return ans