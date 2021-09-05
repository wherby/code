import java.io.BufferedWriter;
import java.io.FileDescriptor;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

object Solution {
    object PersistentArray{
        def test()={
            val NUM = 200000
            var pool: Array[Node] = Array.fill[Node](21 * NUM)(new Node(0,null,null))
            var R = 1000000
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
        //http://www.rgagnon.com/javadetails/java-0603.html
        //https://stackoverflow.com/questions/27628373/why-print-in-scala-is-so-slow

        val out = new BufferedWriter(new OutputStreamWriter(new
         FileOutputStream(java.io.FileDescriptor.out), "ASCII"), 512);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/
        //if val lines = io.Source.fromFile("input/input00.txt").getLines().map{_.split(" ")}.toList there will be timeout 
        val lines = io.Source.fromFile("input/input24.txt").getLines().drop(1).map{ _.split(" ")}.toList
        //val lines = io.Source.stdin.getLines().drop(1).map{ _.split(" ")}.toList
        //print(lines)
        val NUM = 200000
        val pool: Array[Node] = Array.fill[Node](20 * NUM)(new Node(0,null,null))
        val L = 0
        var R = 1000000
        val array = new PersistentArray(pool, 0, R)
        val version = Array.fill[Node](NUM)(new Node(0,null,null))
        val ans = Array.fill[Int](NUM)(0)
        val result = Array.fill[Int](NUM)(0)
        var m =0
        var res = ""
        lines map{
            line=>
            
            if(line(0) == "-"){
                m =m-1
            }else{
                val x = line(1).toInt
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
                //System.out.println(ans(m-1))
                out.write(ans(m-1).toString)
                out.write('\n')
            }else{
                //System.out.println(0)
                out.write("0")
                out.write('\n')
            }

        }
        out.flush()
       // result.map(println)
    }
}