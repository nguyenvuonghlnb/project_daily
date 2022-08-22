module.exports = {
  apps : [
      {
        name: "project_daily_procedure",
        script: "./main.py",
        watch: false,
        instances: 1,
        stop_exit_codes: [0],
        env: {
            app_env: "development"
        }
      }
  ]
}