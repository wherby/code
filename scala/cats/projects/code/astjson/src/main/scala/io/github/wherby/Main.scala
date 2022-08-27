package io.github.wherby


import JsonWriterInstances._
import JsonSyntax._
import io.github.wherby.models.Cat
import io.github.wherby.printable.PrintableInstances._
import io.github.wherby.printable.PrintableSyntax._
//import cats.instances.int._
//import cats.instances.string._
import cats.syntax.show._ // for show
//import cats.implicits._ // This import will change behavior of show



object Main extends App {
  val ret = Person("Dave", "dave@example.com").toJson
  println(ret)
  //println("Hello " |+| "Cats!")
  println(Json.toJson(Option("A string")))
//   val cat = Cat("Garfield", 41, "ginger and black")
// // cat: Cat = Cat("Garfield", 41, "ginger and black")

//   Printable.print(cat)
// // Garfield is a 41 year-old ginger and black cat.

  Cat("Garfield", 41, "ginger and black").print
//  val showInt:Show[Int]= Show.apply[Int]
//  val showString: Show[String] = Show.apply[String]
//
//  val intAsString: String = showInt.show(123)
//  val stringAsString: String = showString.show("abc")
//  val shownInt:String = 123.show
  println(Cat("Garfield", 38, "ginger and black").show)
}
