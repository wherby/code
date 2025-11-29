# 错误的，因为仿射函数没有交换律特性
mod = 10**9+7 
#mod = 998244353

def stackExe(st,eval):
    if len(st)<2:
        return st[0]
    a = st.pop()
    op = st.pop()
    b = st.pop()
    st.append(eval(a,b,op))
    return stackExe(st,eval)


def basicEval(a,b, op):
    if op =="+":
        return a+b 
    return a*b



def affineTEveal(x,y,op):
    
    if op == "+":
        x = x+mod
    else:
        x = x*mod
    xa,xb= divmod(x,mod)
    ya,yb = divmod(y,mod)
    a = xa * ya % mod
    b = (xa * yb + xb) % mod
    return a * mod + b



if __name__ == '__main__':
    import random
    from itertools import zip_longest
    N = 20

    st = [random.randint(1,100) for _ in range(N)]
    opv= "+*"
    ops = [opv[random.randint(0,1)] for _ in range(N-1)]
    result = []
    for num, op in zip_longest(st, ops, fillvalue=None):
        result.append(num)
        if op is not None:
            result.append(op)
    ls= list(result)
    
    #ls= [47, '*', 23, '*', 36, '*', 90, '*', 96, '+', 81, '*', 16, '+', 59, '+', 28, '+', 66, '+', 43, '*', 67, '*', 7, '+', 59, '*', 10, '+', 10, '*', 96, '+', 55, '+', 55, '*', 79]
    
    x1 = stackExe(list(ls),basicEval)
    print(ls)
    ls2 = list(ls)
    ls2[-1] += mod 
    print(ls2)
    x2 = stackExe(list(ls2),affineTEveal)
    print(x1,x2)
    print(x1%mod,x2%mod)
    
