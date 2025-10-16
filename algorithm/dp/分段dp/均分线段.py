
# https://codeforces.com/gym/102409/problem/J

ls  =[0,3,4,5,8,10,12,15,18]
n = len(ls)
lm,rm = 1,3
mx = ls[-1]
for i in range(2,n-2):
    while lm < i-1 and abs((ls[i] - ls[lm]) - (ls[lm] -ls[0])) > abs((ls[i] - ls[lm+1]) - (ls[lm+1] -ls[0])):
        lm +=1
    while rm < n-1 and abs((ls[-1] - ls[rm]) -(ls[rm] - ls[i])) > abs((ls[-1] - ls[rm+1]) -(ls[rm+1] - ls[i])):
        rm +=1
    print(lm,rm)
    ct = [(ls[-1] - ls[rm]) , (ls[rm] - ls[i]),(ls[i] - ls[lm]) , (ls[lm] -ls[0])]
    mx  = min(mx,max(ct) - min(ct))
print(mx)