
def permutete(n):
    order=[0]*n
    chosen = [0]*n
    
    def calc(k):
        if k == n:
            print(order)
            return
        for i in range(n):
            if chosen[i] : continue
            order[k] =i
            chosen[i] =1
            calc(k+1)
            chosen[i] =0
            order[k] =0 ## can be removed
    calc(0)


permutete(4) 
