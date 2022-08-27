package io.github.wherby.models

import cats.Show

import java.util.Date

/**
 * Copyright (c) 2020
 * For io.github.wherby.models in astjson
 * Created by wherby on 2022/8/27
 */
object DateShow {
  implicit val dateShow: Show[Date] =
    new Show[Date] {
      def show(date: Date): String =
        s"${date.getTime}ms since the epoch."
    }
}
