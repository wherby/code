def doSomething(st):
    print(st)

def getSub(state):
    subset =state
    while subset>0:
        doSomething(subset)
        subset = (subset)-1 &state

getSub(7)
getSub(5)
getSub(1)



# while subset>0:
#     if dp[i-1][state-subset] == False:
#         subset = (subset)-1 &state                   ## If need continue to bypass under some condition, the next subset need to be evaluated, otherwise ... loop forever.
#         continue              
#     if canSatisfy(ls[i-1],subset,quantity):
#         dp[i][state] = True
#         break
#     subset = (subset)-1 &state