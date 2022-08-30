package io.github.wherby.moniod

/**
 * Copyright (c) 2020
 * For io.github.wherby.moniod in astjson
 * Created by wherby on 2022/8/27
 */
trait Monoid[A] extends Semigroup[A] {
  def empty: A
}
trait Semigroup[A] {
  def combine(x: A, y: A): A
}

object Monoid {
  def apply[A](implicit monoid: Monoid[A]) =
    monoid

  //Boolean
  implicit val booleanAndMonoid: Monoid[Boolean] =
    new Monoid[Boolean] {
      def combine(a: Boolean, b: Boolean) = a && b
      def empty = true
    }
  implicit val booleanOrMonoid: Monoid[Boolean] =
    new Monoid[Boolean] {
      def combine(a: Boolean, b: Boolean) = a || b
      def empty = false
    }
  implicit val booleanEitherMonoid: Monoid[Boolean] =
    new Monoid[Boolean] {
      def combine(a: Boolean, b: Boolean) =
        (a && !b) || (!a && b)

      def empty = false
    }
  implicit val booleanXnorMonoid: Monoid[Boolean] =
    new Monoid[Boolean] {
      def combine(a: Boolean, b: Boolean) =
        (!a || b) && (a || !b)

      def empty = true
    }

  //set
  implicit def setUnionMonoid[A]: Monoid[Set[A]] =
    new Monoid[Set[A]] {
      def combine(a: Set[A], b: Set[A]) = a union b
      def empty = Set.empty[A]
    }
//  implicit def setIntersectionSemigroup[A]: Semigroup[Set[A]] =
//    new Semigroup[Set[A]] {
//      def combine(a: Set[A], b: Set[A]) =
//        a intersect b
//    }
//  implicit def symDiffMonoid[A]: Monoid[Set[A]] =
//    new Monoid[Set[A]] {
//      def combine(a: Set[A], b: Set[A]): Set[A] =
//        (a diff b) union (b diff a)
//      def empty: Set[A] = Set.empty
//    }

}