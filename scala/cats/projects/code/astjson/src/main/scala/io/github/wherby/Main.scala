package io.github.wherby

import cats.implicits._
import JsonWriterInstances._
import JsonSyntax._
import io.github.wherby.models.Cat
import io.github.wherby.printable.Printable
import io.github.wherby.printable.PrintableInstances._

object Main extends App {
  val ret = Person("Dave", "dave@example.com").toJson
  println(ret)
  println("Hello " |+| "Cats!")
  println(Json.toJson(Option("A string")))
  val cat = Cat("Garfield", 41, "ginger and black")
// cat: Cat = Cat("Garfield", 41, "ginger and black")

  Printable.print(cat)
// Garfield is a 41 year-old ginger and black cat.
}
