############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(list(map(int,input().split())))

def resolve():
    key=inp()
    ls = invr()
    st=set()
    if key ==0:
        return "NO"
    while key not in st:
        st.add(key)
        key = ls[key-1]
        if key ==0:
            break
        
        
    if len(st) ==3:
        return "YES"
    else:
        return "No"
    

def op(caseidx):
    ret= resolve()
    print(ret)
    

for i in range(int(input())):
    op(i)