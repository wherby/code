# https://codeforces.com/gym/106592/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0622/solution/cf106592c.md
# 这里使用二分变量特殊的设置方式，使得选r作为削峰的上限的时候，一定还有剩余的值没有分配的
# 因为二分的时候，如果分配有剩余，则r的值会比这个值少，所以r的值就保证最多是小于等于期望分配的值



def main():
    t = II()
    outs = []
    
    for _ in range(t):
        k, n = MII()
        nums = LII()
        
        l, r = 0, 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            
            val = 0
            for x in nums:
                val += fmin(x, mid)
            
            if val > k: r = mid - 1
            else: l = mid + 1
    
        ans = [fmin(v, r) for v in nums]
        k -= sum(ans)
        
        for i in range(n):
            if ans[i] < nums[i] and k:
                k -= 1
                ans[i] += 1
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))