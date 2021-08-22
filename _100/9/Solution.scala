object Solution {
  def isPalindrome(x: Int): Boolean = {
    if (x < 0) {
      return false
    }
    var re = x
    var res: Seq[Int] = Seq()
    while (re > 0) {
      res = res :+ re % 10
      re = re / 10
    }
    val n = res.length
    for (i <- 0 until n) {
      if (res(i) != res(n - 1 - i)) {
        return false
      }
    }
    return true
  }
}

object Test extends App {
  val s = Solution.isPalindrome(121)
  println(s)
}
