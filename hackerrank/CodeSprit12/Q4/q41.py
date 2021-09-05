

mem =[-1]*1000

def factorial(n):
    global mem
    if n ==1 :
        return 1
    MOD =10**9
    if mem[n] != -1:
        return mem[n]
    else:
        mem[n]= n * factorial(n-1) %MOD
        return mem[n]
    
for i in range(1,41):
    print factorial(i)