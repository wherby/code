package io.github.wherby



import io.github.wherby.test.{FutureTest, PrintTest, SetMonoidTest, ShowTest, TestCat, TestEq, TestMonoid2}
//import cats.instances.int._
//import cats.instances.string._
//import cats.implicits._ // This import will change behavior of show



object Main extends App {

  PrintTest.testPrint()
  ShowTest.testShow()
  TestEq.testEq()
  SetMonoidTest.testSetMonoid()
  TestCat.test1()
  TestMonoid2.testMonoid()
  FutureTest.testFuture()
}
