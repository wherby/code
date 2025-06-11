from collections import Counter
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        tar= ["0","1","2","3","4"]
        ret = -10**10
        
        for a in tar:# odd
            for b in tar: # even
                if a == b : continue
                c = Counter()
                c2 = Counter()
                ls = [-10**10]*4
                ls[0]=0
                left = 0
                for i,a1 in enumerate(s):
                    c[a1] +=1
                    tick = c[a]%2 *2  +c[b]%2
                    while i-k>=left and c2[a] + int(s[left]==a) +1<=c[a] and c2[b]+1+ int(s[left] ==b) <=c[b] :
                        c2[s[left]] +=1
                        tick2 = c2[a]%2 *2  +c2[b]%2
                        ls[tick2] = max(ls[tick2], -c2[a] +c2[b])
                        left +=1
                    if i >=k-1 and c[b]>=2 and c[a]>=1:
                        #print(ret,tick,ls,i)
                        ret = max(ret, c[a]-c[b]+ls[(2+tick)%4])
                        #print(ls,ret,c[a]-c[b],ls[(2+tick)%4],c[a],c[b],c[a]-c[b]+ls[(2+tick)%4],a,b)
                    
        return ret


# 2->0
# 3->1
# 0->2
# 1->3

re = Solution().maxDifference("2222130",2)
print(re)