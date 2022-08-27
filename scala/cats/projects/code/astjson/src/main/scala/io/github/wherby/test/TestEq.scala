package io.github.wherby.test

import cats.Eq
import cats.instances.int._
import cats.syntax.eq._
import cats.instances.option._

import java.util.Date // for Eq
import io.github.wherby.models.DateShow._
/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object TestEq {
 def testEq()={
   val eqInt = Eq[Int]
   println(eqInt.eqv(123,123))
   println(123 === 123)
   println((Some(1):Option[Int])===(None:Option[Int]))
   val x = new Date() // now
   Thread.sleep(100)
   val y = new Date() // a bit later than now
   println(x===x)
   println(x ===y )
 }
}
