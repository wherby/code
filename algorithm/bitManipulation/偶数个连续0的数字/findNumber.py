def findNumber(m):
    in_s = [0]* (1<<m)
    for i in range(1<<m):
        cnt,has_odd =0,0
        for j in range(m):
            if(i>>j &1):
                has_odd |= cnt 
                cnt =0 
            else:
                cnt ^=1
        in_s[i] = 0 if has_odd | cnt else 1
    for i in range(1<<m):
        print(in_s[i],bin(i))

findNumber(4)

print(0^1)
print(1^1)
print(1^1)