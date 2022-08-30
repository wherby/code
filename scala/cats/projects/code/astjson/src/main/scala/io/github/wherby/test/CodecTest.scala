package io.github.wherby.test

import io.github.wherby.moniod.Box
import io.github.wherby.moniod.Codec._

/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object CodecTest {
  def testCodec()={
    encode(123.4)
    // res11: String = "123.4"
    decode[Double]("123.4")
    // res12: Double = 123.4

    encode(Box(123.4))
    // res13: String = "123.4"
    decode[Box[Double]]("123.4")
    // res14: Box[Double] = Box(123.4)
  }
}
