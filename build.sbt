val appName = "ctc-traders-phase5-tis"

lazy val microservice = Project(appName, file("."))
  .enablePlugins(play.sbt.PlayScala, SbtAutoBuildPlugin, SbtDistributablesPlugin)
  .settings(
    libraryDependencies ++= AppDependencies.compile ++ AppDependencies.test,
    update / evictionWarningOptions := EvictionWarningOptions.default.withWarnScalaVersionEviction(false),
    majorVersion := 0,
    scalaVersion := "2.13.8",
    scalacOptions ++= Seq(
      "-Xfatal-warnings",
      "-Wconf:src=routes/.*:silent",
      "-feature"
    )
  )
  .settings(
    resolvers += Resolver.jcenterRepo
  )
