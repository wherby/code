package io.github.wherby
//https://github.com/jsuereth/scala-in-depth-source/blob/master/chapter6/existential-types/existential.scala
/**
 * Copyright (c) 2020
 * For io.github.wherby in scalaindepth
 * Created by wherby on 2022/9/24
 */
object ObservableTest {
  def testObservable()={
    val x = new VariableStore(12)
    val d = new Dependencies{}
    val t= x.observe(println)
    d.addHandle(t) //Not working.
    val t2 = x.observe(println)
    d.addHandle(t2)
    x.set(3)
    d.removeDependencies()
    x.set(2)
  }

}
