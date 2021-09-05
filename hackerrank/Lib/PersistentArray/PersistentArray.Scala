
object PersistentArray{
    def main(args: Array[String]) {
        print("test")
        test()
    }

    def test()={
        val NUM = 200000
        var pool: Array[Node] = Array.fill[Node](20 * NUM)(new Node(0,null,null))
        var R = 10000000
        val array = new PersistentArray(pool, 0, R)
        var version = Array.fill[Node](11)(new Node(0,null,null))
        var root = array.GetNewNode()
        for(i <- 0 to 10){
            root = array.upd(root,0,R, i,i)
            version(i) = root
            for(j <- 0 to 10){
                print(array.get(root,0,R,j))
                println("")

            }
            println()
        }
    }
}
 


class PersistentArray( pool: Array[Node], L: Int, R: Int){
    class Node(valueV: Int,leftV: Node, rightV: Node){
        var value = valueV
        var left = leftV
        var right = rightV
    }
    
    var lastUsed = -1 //to kept the new node from 0
    def GetNewNode():Node={
        lastUsed = lastUsed +1 
        pool(lastUsed)
    }

    def get(v: Node, l : Int, r: Int, at: Int):Int={
        if(v == null)return 0

        if(l+1 ==r){
            return v.value
        }

        val m = (l + r)/2
        if( at < m){
            return get(v.left,l,m,at)
        }else{
            return get(v.right,m,r,at)
        }
    }

    def upd(v: Node, l: Int, r: Int, at: Int, value: Int):Node={
        var res = GetNewNode()

        if(v != null){
            res = v
        }

        if(l + 1 == r){
            res.value = value
            return res
        }

        val m = (l + r )/2

        if(at < m){
            res.left = upd(res.left,l,m,at,value)
        }else{
            res.right = upd(res.right,m,r, at,value)
        }
        res
    }
}