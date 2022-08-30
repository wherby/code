package io.github.wherby.test

import cats.Eq
import cats.instances.int._
import cats.syntax.eq._
import cats.instances.option._

import java.util.Date
import io.github.wherby.models.DateShow._

import io.github.wherby.models.Cat // for Eq
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
   val cat1 = Cat("Garfield",   38, "orange and black")
   // cat1: Cat = Cat("Garfield", 38, "orange and black")
   val cat2 = Cat("Heathcliff", 32, "orange and black")
   // cat2: Cat = Cat("Heathcliff", 32, "orange and black")

   cat1 === cat2
   // res15: Boolean = false
   cat1 =!= cat2
   // res16: Boolean = true
   val optionCat1 = Option(cat1)
   // optionCat1: Option[Cat] = Some(Cat("Garfield", 38, "orange and black"))
   val optionCat2 = Option.empty[Cat]
   // optionCat2: Option[Cat] = None

   println(optionCat1 === optionCat2)
   // res17: Boolean = false
   println( optionCat1 =!= optionCat2)
   // res18: Boolean = true
 }
}
