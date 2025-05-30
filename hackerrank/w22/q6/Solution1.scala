object Solution {
    object PersistentArray{
        def test()={
            val NUM = 200000
            var pool: Array[Node] = Array.fill[Node](23 * NUM)(new Node(0,null,null))
            var R = 10000000
            val array = new PersistentArray(pool, 0, R)
            var version = Array.fill[Node](11)(new Node(0,null,null))
            var root = array.GetNewNode()
            for(i <- 0 to 10){
                root = array.upd(root,0,R, i,i)
                version(i) = root
                for(j <- 0 to 10){
                    print(array.get(root,0,R,j))
                    print("")

                }
                println()
            }
        }
    }
 

    class Node(valueV: Int,leftV: Node, rightV: Node){
        var value = valueV
        var left = leftV
        var right = rightV
    }
    class PersistentArray( pool: Array[Node], L: Int, R: Int){

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
                // need to shallow copy of v:   *res = *v in go lang
                res.value = v.value
                res.left = v.left
                res.right = v.right
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
            return res
        }
    }

    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/
        //if val lines = io.Source.fromFile("input/input00.txt").getLines().map{_.split(" ")}.toList there will be timeout 
        val lines = io.Source.fromFile("input/input00.txt").getLines().map{_.split(" ")}.toArray
        //val lines = io.Source.stdin.getLines().map{_.split(" ")}.toArray
        //print(lines)
        val NUM = lines(0)(0).toInt
        val pool: Array[Node] = Array.fill[Node](22 * NUM)(new Node(0,null,null))
        val L = 0
        val R = 1000000
        val array = new PersistentArray(pool, 0, R)
        val version = Array.fill[Node](NUM)(new Node(0,null,null))
        val ans = Array.fill[Int](NUM)(0)
        val result = Array.fill[Int](NUM)(0)
        var m =0
        var res = ""
        for(i <- 1 to NUM){
            if(lines(i)(0) == "-"){
                m =m-1
            }else{
                val x = lines(i)(1).toInt
                if( m == 0){
                    version(m) = array.upd(null,L,R,x,1)
                }else{
                    val j = ans(m-1)
                    version(m) = array.upd(version(j),L,R,x,m+1)
                    ans(m) = array.get(version(j),L,R,x)
                }
                m =m+1
            }
            if(m>0){
                result(i-1) = ans(m-1)
            }else{
                result(i-1) = 0
            }

        }
        result.map(println)
    }
}