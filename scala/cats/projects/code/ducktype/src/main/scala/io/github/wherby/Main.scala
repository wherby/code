package io.github.wherby

import cats.instances.string._
import cats.syntax.semigroup._

import java.io.{File, FileWriter}
import scala.language.reflectiveCalls

object Main extends App {
  val writer = new FileWriter(new File("Main.scala"))
  Resources.clouseResource(writer)
  println("Hello " |+| "Cats!")

}

object Resources{
  type Resource ={
    def close(): Unit
  }
  def clouseResource(r:Resource) ={
    println("Resource closing")
    r.close()
    println("Resource closed")
  } 
}
