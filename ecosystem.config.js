module.exports = {
  apps : [
      {
        name: "project_daily_procedure",
        script: "./main.py",
        watch: false,
        instances: 1,
        cron_restart: "00 07 * * *",
        stop_exit_codes: [0],
        env: {
            app_env: "production"
        }
      }
  ]
}