import json,os,ast,time,warnings

import requests
from bs4 import BeautifulSoup

from telethon import TelegramClient, sync, events
from telethon.sync import TelegramClient

from config_parcer import url, name_chat, path_logs, api_id, api_hash

warnings.simplefilter('ignore', category=UserWarning)

print('''

██████╗░░█████╗░██████╗░░█████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝██║░░╚═╝█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔══██╗██║░░██╗██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░██║╚█████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
              by Onione Tamiko
''')


def Start():
    username_tg = str(api_id)
    bot = TelegramClient(username_tg, api_id, api_hash)
    print("Запуск Парсера успешно завершен...")
    bot.start()
    bot.send_message(name_chat,"Парсер начал подглядывать за вашим сервером...")
    bot.disconnect()
    log_line_old = 0
    a = 0
    while True:
        time.sleep(0.4)
        with open(path_logs, 'r',encoding='utf-8') as f:
            last_line = f.readlines()[-1]
            if last_line == log_line_old:
                pass
            else:
                if a>=1:
                    sms_send = last_line.strip()
                    sms_send = sms_send.split('<')
                    name_account = sms_send[0].split(' ')[-1]
                    date = sms_send[0].split(' ')[1]
                    time_drop = sms_send[0].split(' ')[3]
                    id_item = sms_send[3].split('[')[1].split(']')[0]
                    id_settings = id_item.split('-')
                    
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find('li', class_=f'q{id_settings[3]} i{id_settings[0]}')
                    name_drop = quotes.find('em').text

                    drop_sms = f"{name_account} получил  {name_drop}"
                    print(drop_sms)
                    bot.start()
                    bot.send_message(name_chat,drop_sms)
                    bot.disconnect()
                log_line_old = last_line
                a+=1
                
    print("PARCER ЗАВЕРШИЛ РАБОТУ...")

Start()

