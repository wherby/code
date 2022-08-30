package io.github.wherby.test

import io.github.wherby.moniod.Monoid

/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object SetMonoidTest {
  def testSetMonoid()={
    val intSetMonoid = Monoid[Set[Int]]
    val strSetMonoid = Monoid[Set[String]]
    println(intSetMonoid.combine(Set(1, 2), Set(2, 3)))
    println(strSetMonoid.combine(Set("A", "B"), Set("B", "C")))
  }
}
