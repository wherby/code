package io.github.wherby.test
import cats._
import cats.implicits._
import cats.instances.map._
/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object TestMonoid2 {
  def testMonoid()={
    val stringResult = "Hi " |+| "there" |+| Monoid[String].empty
    println(stringResult)
    val intResult = 1 |+| 2 |+| Monoid[Int].empty
    println(intResult)
    val map1 = Map("a" -> 1, "b" -> 2)
    val map2 = Map("b" -> 3, "d" -> 4)

    val map3= map1 |+| map2
    println(map3)
  }
}
