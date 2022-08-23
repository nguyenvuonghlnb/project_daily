import service
import database
import telegram
from datetime import datetime


def miss():
    print("Done insert data miss", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), )
    telegram.send(mess="Đang test xem thế nào two !")