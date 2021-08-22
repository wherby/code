sealed trait TreeNodeT
case class Node[T](value: T) extends TreeNodeT
case class TreeNode[T](node: Node[T], children: Seq[TreeNode[T]] = Seq())
    extends TreeNodeT

object Test extends App {

  def traverse[T](root: TreeNode[T], res: Seq[T]): Seq[T] = {
    var rest = res :+ root.node.value
    root.children.map { child =>
      rest = traverse(child, rest)
    }
    rest
  }

  val tree = TreeNode(Node(1), Seq(TreeNode(Node(2)), TreeNode(Node(3))))
  println(tree)
  val res = traverse(tree, Seq())
  println(res)
}
