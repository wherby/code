package io.github.wherby

import cats.implicits._
import JsonWriterInstances._
import JsonSyntax._


object Main extends App {
  val ret = Person("Dave", "dave@example.com").toJson
  println(ret)
  println("Hello " |+| "Cats!")
}
