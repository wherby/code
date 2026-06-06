# f(x) = x(1-0.013*x)



def f(x):
    if (1-0.013*x)<0:
        return 0
    return x*(1-0.013*x)
    
left ,right =1,1/0.013 
for _ in range(100):
    mid1 = (left * 2 + right) / 3
    mid2 = (left + right * 2) / 3
    
    if f(mid1) >f(mid2): right = mid2
    else: left = mid1
    print(mid1,mid2,f(mid1) , f(mid2))

print(left,right)
print(f(38.46),f(76.9))
mx = 0 
ret = 0
for i in range(1000):
    if f(i)>mx:
        mx = f(i)
        ret = i
print(ret,f(ret))