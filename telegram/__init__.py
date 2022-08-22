import requests


def send(mess):
    chat_id = '-623141295'
    token = '5514118291:AAGhg7iZX2mHUXszI_hrDY6efTXkEIYEhCg'
    # msg = "Send text with photo 😉"
    telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mess}')
    # print(telegram_msg)
    # print(telegram_msg.content)

