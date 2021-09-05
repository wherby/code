import play.api.libs.json.Json
def add(requst:String):Option[Int]={
  val inputParas = Json.parse(requst)
  val a = (inputParas   \ "a").asOpt[Int]
  val b = (inputParas \ "b").asOpt[Int]
  (a,b) match {
    case (a1:Some[Int],b1:Some[Int])=>Some(a1.get +b1.get)
    case _=>None
  }
}