import itertools
class Solution:
    def maxProduct(self, s):
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i])
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:2]
    
        def helper(s):
            man, n = manachers(s),len(s)
            ints = [(i-man[i]//2, i+man[i]//2) for i in range(n)]
            #print(ints)
            arr =[0]*n
            for a,b in ints:
                arr[b] = max(arr[b],b-a +1)
            #print(arr,"aa")
            for i in range(n-2,-1,-1):
                arr[i] = max(arr[i],arr[i+1]-2) # If there is no longer palindromic string, then the length will be smaller than 2 for odd length in the question. 
            #print(arr,"bb")
            return list(itertools.accumulate(arr,max))
        
        t1,t2 = helper(s),helper(s[::-1])[::-1][1:] +[0]
        #print(t1)
        return max(x*y for x,y in zip(t1,t2))


print(Solution().maxProduct("ababbb"))