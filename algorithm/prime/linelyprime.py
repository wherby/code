#https://blog.csdn.net/qq_51537085/article/details/115749091?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.no_search_link&spm=1001.2101.3001.4242.0



def get_prime(n):
    cnt =0
    prime=[0]*(n+2)
    st = [False] *(n+2)

    for i in range(2,n+1):
        if not st[i]:
            cnt +=1
            prime[cnt] =i
            
        j = 1
        while prime[j] <= n/i:
            st[prime[j]*i] =True
            if i % prime[j] ==0:
                break
            j +=1
    print(prime[:1000])

get_prime(1000000)