object App{
    sealed trait Ops
    case class Op1(a:Int,b:Int) extends Ops
    case class Op2(a:Int,b:Int) extends Ops
    val maxLen = 100

    val lockP = Op1(1)
    val lockP2 = Op1(2)
    def processMethod(queue:Seq[Ops]):Option[Result]={
        while(queue.isEmpty){
            await queue
        }
        Thread.holdsLock(lockP){
            val head = queue.head
            queue.drop(1)
        }
        val res = eval(queue.head)
        return Some(res)
       
    }

    def postRequst(queue:Seq[Ops], ops:Seq[Ops]):Boolean ={
        Thread.holdsLock(lockP2){
            if(queue.length < maxLen){
                queue = queue :+ ops
                true
            }else{
                false
            }
        }
    }
}