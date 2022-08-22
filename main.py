import time
import schedule
import config
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from controller import message

scheduler = BlockingScheduler(timezone='Asia/Ho_Chi_Minh')
now = datetime.now()
print("Start deploying !", now.strftime('%Y-%m-%d %H:%M:%S'))


def import_message():
    message.daily()


# if __name__ == '__main__':
#     import_message()


# /Financial: 10min/time 09h-18h 02
# scheduler.add_job(import_financial_datas_min, 'cron', day_of_week='mon-sun', hour='09-18', minute='1-51/10', start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# # /Message: 15min/time 08h-18h 01
scheduler.add_job(import_message, 'cron', day_of_week='mon-sun', hour='08-18', minute='2-47/15', start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# # /CorporateAction: 40min/time 09h-18h 06
# scheduler.add_job(import_corporate_action_datas, 'cron', day_of_week='mon-sun', hour='09-18', minute='0-59/40', start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# # /Company: 1h/time 09h-18h 02
# scheduler.add_job(import_company_datas, 'cron', day_of_week='mon-sun', hour='09-19', minute=3, start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# # /Ratio: Call 2 time 18h, 21h 04
# scheduler.add_job(import_ratio_datas, 'cron', day_of_week='mon-sun', hour='18-22', minute=4, start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# # /Market: Call 3 time 15h30, 17h30, 19h30 05
# scheduler.add_job(import_market_datas, 'cron', day_of_week='mon-sun', hour='15-20', minute=33, start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# scheduler.add_job(import_market_datas, 'cron', day_of_week='mon-sun', hour='15-20', minute=33, start_date='2022-08-18 08:00:00', end_date='2023-08-18 08:00:00')
# Start the scheduler
scheduler.start()


# def job_message():
#     now = datetime.now(import_message_datas())
#     datetime_string = now.strftime('%Y-%m-%d %H:%M:%S')
#     print("Insert data /Messages !", datetime_string)

# def schedule_messages_15minutes():  # /Message: 15min/time 08h-18h
#     job_message()
#     schedule.every(15).minutes.until("18:00").do(job_message)
#     print("---------------15 minutes/time 08h to 18h---------------")
#     return schedule.CancelJob

# while True:
#     schedule.run_pending()
#     time.sleep(1)
