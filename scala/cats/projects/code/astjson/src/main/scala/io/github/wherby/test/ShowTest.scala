package io.github.wherby.test

import cats.implicits.toShow

import java.util.Date
import io.github.wherby.models.{Cat}
import io.github.wherby.models.DateShow.dateShow

/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object ShowTest {
  def testShow()={
    println(Cat("Garfield", 38, "ginger and black").show)
    new Date().show
  }
}
