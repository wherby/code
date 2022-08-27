package io.github.wherby.test

import io.github.wherby.JsonSyntax.JsonWriterOps
import io.github.wherby.JsonWriterInstances.{optionWriter, personWriter, stringWriter}
import io.github.wherby.{Json,  Person}
import io.github.wherby.models.Cat
import io.github.wherby.printable.PrintableInstances._
import io.github.wherby.printable.PrintableSyntax._
/**
 * Copyright (c) 2020
 * For io.github.wherby.test in astjson
 * Created by wherby on 2022/8/27
 */
object PrintTest {
  def testPrint()={
    val ret = Person("Dave", "dave@example.com").toJson
    println(ret)
    //println("Hello " |+| "Cats!")
    println(Json.toJson(Option("A string")))
    //   val cat = Cat("Garfield", 41, "ginger and black")
    // // cat: Cat = Cat("Garfield", 41, "ginger and black")

    //   Printable.print(cat)
    // // Garfield is a 41 year-old ginger and black cat.

    Cat("Garfield", 41, "ginger and black").print
  }
}
