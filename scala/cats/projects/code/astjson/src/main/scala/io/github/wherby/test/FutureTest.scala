package io.github.wherby.test

import scala.util.Random

import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._
/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 * https://www.scalawithcats.com/dist/scala-with-cats.html
Futures and Referential Transparency

Note that Scala’s Futures aren’t a great example of pure functional programming because they aren’t referentially transparent. Future always computes and caches a result and there’s no way for us to tweak this behaviour. This means we can get unpredictable results when we use Future to wrap side-effecting computations. For example:

import scala.util.Random

val future1 = {
  // Initialize Random with a fixed seed:
  val r = new Random(0L)

  // nextInt has the side-effect of moving to
  // the next random number in the sequence:
  val x = Future(r.nextInt)

  for {
    a <- x
    b <- x
  } yield (a, b)
}

val future2 = {
  val r = new Random(0L)

  for {
    a <- Future(r.nextInt)
    b <- Future(r.nextInt)
  } yield (a, b)
}

val result1 = Await.result(future1, 1.second)
// result1: (Int, Int) = (-1155484576, -1155484576)
val result2 = Await.result(future2, 1.second)
// result2: (Int, Int) = (-1155484576, -723955400)
Ideally we would like result1 and result2 to contain the same value. However, the computation for future1 calls nextInt once and the computation for future2 calls it twice. Because nextInt returns a different result every time we get a different result in each case.

This kind of discrepancy makes it hard to reason about programs involving Futures and side-effects. There also are other problematic aspects of Future's behaviour, such as the way it always starts computations immediately rather than allowing the user to dictate when the program should run. For more information see this excellent Reddit answer by Rob Norris.

When we look at Cats Effect we’ll see that the IO type solves these problems.
 */
object FutureTest {
  def testFuture()={
    val future1 = {
      // Initialize Random with a fixed seed:
      val r = new Random(0L)

      // nextInt has the side-effect of moving to
      // the next random number in the sequence:
      val x = Future(r.nextInt())

      for {
        a <- x
        b <- x
      } yield (a, b)
    }

    val future2 = {
      val r = new Random(0L)

      for {
        a <- Future(r.nextInt())
        b <- Future(r.nextInt())
      } yield (a, b)
    }

    val result1 = Await.result(future1, 1.second)
    // result1: (Int, Int) = (-1155484576, -1155484576)
    val result2 = Await.result(future2, 1.second)
    // result2: (Int, Int) = (-1155484576, -723955400)
    println((result1,result2))
  }
}
