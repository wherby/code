package io.github.wherby.test

import cats.implicits.toFunctorOps
import io.github.wherby.models.{ Tree}
import io.github.wherby.models.Tree._

/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object TreeTest {
  def testTree()={
    Tree.leaf(100).map(_ * 2)
    // res9: Tree[Int] = Leaf(200)

    println(Tree.branch(Tree.leaf(10), Tree.leaf(20)).map(_ * 2))
    // res10: Tree[Int] = Branch(Leaf(20), Leaf(40))
  }
}
