package io.github.wherby



import io.github.wherby.test.{PrintTest, ShowTest, TestEq}
//import cats.instances.int._
//import cats.instances.string._
//import cats.implicits._ // This import will change behavior of show



object Main extends App {

  PrintTest.testPrint()
  ShowTest.testShow()
  TestEq.testEq()
}
