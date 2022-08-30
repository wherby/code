

## Dock type
code:
```scala
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
```

```
    PS C:\Users\where\Documents\github\code\scala\cats\projects\code\ducktype> sbt run 
    [info] Loading global plugins from C:\Users\where\.sbt\1.0\plugins
    [info] Loading settings for project ducktype-build from plugins.sbt ...
    [info] Loading project definition from C:\Users\where\Documents\github\code\scala\cats\projects\code\ducktype\project
    [info] Loading settings for project ducktype from build.sbt ...
    [info] Set current project to ducktype (in build file:/C:/Users/where/Documents/github/code/scala/cats/projects/code/ducktype/)
    [info] running io.github.wherby.Main 
    Resource closing
    Resource closed
    Hello Cats!
    [success] Total time: 1 s, completed 2022-8-27 13:58:47
```