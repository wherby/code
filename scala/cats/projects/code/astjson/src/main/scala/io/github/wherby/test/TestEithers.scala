package io.github.wherby.test

import cats.syntax.either._
/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/9/3
 */
object TestEithers extends App{
  def eitherTest(): Unit ={
    val a1=  "Error".asLeft[Int].getOrElse(0)
    val a2 = "error".asLeft[Int].recover {
      case _: String => -1
    }
    println(a1)
    println(a2)
    val a3 = for {
      a <- 1.asRight[String]
      b <- 0.asRight[String]
      _ <- if(b == 0) "DIV0".asLeft[Int]
      else (a / b).asRight[String]
    } yield a* 100
    println(a3)
    val a4 = for {
      a <- 1.asRight[String]
      b <- 1.asRight[String]
      c <- if(b == 0) "DIV0".asLeft[Int]
      else (a / b).asRight[String]
    } yield c * 100
    println(a4)
  }
  eitherTest()
}
