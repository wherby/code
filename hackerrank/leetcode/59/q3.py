# Count Different Palindomic Subsequences String
#https://discuss.leetcode.com/topic/111217/n-2-dp-python-with-explanation
#Let dp(i, j) be the answer for the string T = S[i:j+1] including the empty sequence.
# The answer is the number of unique characters in T, plus dp(next('a', i) + 1, 
#prev('a', j) - 1) representing palindromes of the form "a_a"
# where _ is zero or more characters, plus dp(next('b', i) + 1, prev('b', j) - 1) 
#representing "b_b", etc.

#Here, next('a', i) means the next index at or after i where A[next('a', i)] = 'a',
# and so on.

class Solution(object):
    def countPalindromicSubsequences(self, S):
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N
    
        last = [None] * 4
        for i in xrange(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [None] * 4
        for i in xrange(N-1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)
        
        MOD = 10**9 + 7
        memo = [[None] * N for _ in xrange(N)]
        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i <= j:
                for x in xrange(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1
                    if None < i0 < j0:  # If not empty string
                        ans += dp(i0+1, j0-1)
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N-1) - 1

if __name__=="__main__":
    s = Solution()
    print s.countPalindromicSubsequences("abcdabcaaa")