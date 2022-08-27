package io.github.wherby.test

import cats.Monoid
import cats.instances.string._ // for Monoid

/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 * https://www.scalawithcats.com/dist/scala-with-cats.html
As always, unless we have a good reason to import individual instances, we can just import everything.

import cats._
import cats.implicits._
 */
class CatMonoidTest {
  def catmonoidTest()={
    println( Monoid[String].combine("hi","their"))
  }
}
