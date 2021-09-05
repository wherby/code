n = int(raw_input())
test = raw_input()
a = test.split()
val = a[n-1]
for i in range(n-2,-2,-1):
    test=test.split()
    if i == -1:
        test[i+1] = val
        break
    elif int(test[i])>int(val):
        test[i+1]=test[i]
    
    else:
        test[i+1] = val
        break
    test = ' '.join(test)
    print test  
test = ' '.join(test)
print test