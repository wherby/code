name := "test2"
version := "0.0.1-SNAPSHOT"

scalaVersion := "2.13.6"

libraryDependencies += "org.typelevel" %% "cats-core" % "2.6.1"

// scalac options come from the sbt-tpolecat plugin so need to set any here

addCompilerPlugin("org.typelevel" %% "kind-projector" % "0.13.0" cross CrossVersion.full)