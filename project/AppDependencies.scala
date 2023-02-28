import play.sbt.PlayImport._
import sbt._

object AppDependencies {

  val bootStrapPlayVersion = "7.13.0"

  val compile = Seq(
    ws,
    "uk.gov.hmrc" %% "bootstrap-frontend-play-28" % bootStrapPlayVersion)

  val test = Seq(
    "org.scalatest"       %% "scalatest"              % "3.2.11"             % "test",
    "com.vladsch.flexmark" % "flexmark-all"           % "0.62.2"             % "test",
    "uk.gov.hmrc"         %% "bootstrap-test-play-28" % bootStrapPlayVersion % "test"
  )
}
