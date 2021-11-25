#morgan
#stanley
#investment
#bank
#ms mt
#msib msia msin msik msnb 
from typing import Match


def multi(a,ls):
    res = []
    for t in ls:
        res.append(a+t)
    return res

def productList(ls):
    n= len(ls)
    res =[a for a in ls[0]]
    #print(res)
    for i in range(1,n):
        tps = []
        for x in res:
            tp = multi(x,ls[i])
            tps = tps +tp
        #print(tp)
            #res =tps
        res =tps

    #res =multi(res,j)
    print(res)

res = ["morgan","stanley" ,"investment","bank"]
productList(res)


(step1) + (step2) +(step3)

def cal(par)={
    if(cache.get(par)){
        return cache.get()
    }else{
        cache.set(par, future( dojob()))
    }
}
case class(fun1){
    
}

eval{
    case fun1{
        c=> ca
    }
}
seal trait Ops
case class AddFun( par1:Int) extend Ops
case class Mulfun(par1:Int) extend Ops
case class Fun(funs : Seq[Ops])

def evalJob(fun: Seq[Ops]): Future[Int]{
    fun Match{
        case AddFun(par1) :: list => Future[par1+ eval(List)]
        case MulFun(par1)::list => Future[par1 * eval(list)]
        case Nil=>Future[1]
    }
}
    
def eval(fun: Seq[Ops]):Future[Int]={
    if cache.get(fun.tostring) != null{
        cache.get(fun.tostring)
    }esle{
        val res= evalJob(fun)
        cache.set(fun.toString(),res)
        res
    }
}