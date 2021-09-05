z.cn
seller central
z.cn -> order -> seller central  -->    --> carrier







order-> 
Table1(orderID,buyer,count,seller,money,dest)
Table2(orderID,time, status)
Table3(From, To, carriers)

status=[tv:nosend ,machine:nosend, getOrder:machine, getorderTime:time,sellerconfirm:]


FrontEnd 
getOrder
RecordOrder


Backend
RedDB-> carrier


Node( val
left*
right*)


def turn(root,previous):
    if root == null:
        return previous
    previous = turn(root.left,previous)
    root.left = previous
    if previous != null:
        previous.right = root
    previous = root 
    previous = turn(root.right, previous)
    return previous
    
turn(root,null)


def getHigAndPHit(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    n = min(n1,n2)
    hit =0
    phit =0
    for i in range(n):
        if str1[i] == str2[i]:
            hit = hit +1
            str1[i]= '*'
            str2[i]='*'
   str1 = filter(lambda x: x!='*',str1)
   str2 = filter(lambda x:x != '*',str2)
   dic1 = {}
   dic2={}
   for x in str1:
       if x not in dic1:
           dic1[x] =1
       else:
           dic1[x] = dic1[x]+1
   for x in str2:
       if x not in dic2:
           dic2[x] =1
       else:
           dic2[x] =dic2[x]+1
   for key,value in dic1.items():
       if key in dic2:
           value2 = dic2[key]
           phit = phit + min(value,value2)
   return (hit,phit) 