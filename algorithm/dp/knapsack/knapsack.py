def knapsack(bags,total):
    dp = [-10*9]*(total+1)
    dp[0]=0
    for bag in bags:
        value,weight = bag
        for start in range(total-weight,-1,-1): # range裏順序逆序的時候就是每個物品只能選一次，順序的時候是每個物品可以選多次
            dp[start + weight] = max(dp[start+weight],dp[start] + value)
    print(dp)
    return max(dp)

def knapsack2(bags,total):
    dp = [-10*9]*(total+1)
    dp[0]=0
    current = 0  # 用current可以減少計算次數
    for bag in bags:
        value,weight = bag
        for start in range(min(current, total-weight),-1,-1): # range裏順序逆序的時候就是每個物品只能選一次，順序的時候是每個物品可以選多次
            dp[start + weight] = max(dp[start+weight],dp[start] + value)
        current = min(current + weight,total)
    print(dp)
    return max(dp)

bags =[[3,1],[4,2],[5,3],[6,4]]
total = 5
re = knapsack(bags,total)
re2 = knapsack2(bags,total)
print(re,re2)