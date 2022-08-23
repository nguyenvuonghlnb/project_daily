import service
import database
import telegram
from datetime import datetime


def daily():
    print("Done insert data daily", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), )
    telegram.send(mess="Đang test xem thế nào one !")

