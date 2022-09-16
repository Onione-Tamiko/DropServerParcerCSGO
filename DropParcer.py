import json, os, ast, warnings, win32gui, win32process, datetime, requests

from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime, date
from telethon import TelegramClient, sync, events
from telethon.sync import TelegramClient

from config_parcer import url, name_chat, path_logs, api_id, api_hash

warnings.simplefilter('ignore', category=UserWarning)

def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        win32gui.SetWindowText(hwnd,'Drop Parcer for Server  |  by Onione Tamiko')

pid = os.getppid()        
win32gui.EnumWindows(enum_window_callback, pid)

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
##    bot.start()
##    bot.send_message(name_chat,"Парсер начал подглядывать за вашим сервером...")
##    bot.disconnect()
    a = sum(1 for line in open(path_logs, 'r',encoding='utf-8'))
    while True:
        sleep(1)
        try:
            if a == sum(1 for line in open(path_logs, 'r',encoding='utf-8')):
                pass
            else:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')
                with open(path_logs, 'r',encoding='utf-8') as f:
                    col_read = int(sum(1 for line in open(path_logs, 'r',encoding='utf-8'))) - int(a)
                    lines = f.readlines()
                    
                for item in range(col_read):
                    item += 1
                    last_line = lines[int(-item)]

                    sms_send = last_line.strip()
                    sms_send = sms_send.split('<')
                    name_account = sms_send[0].split('Игроку')[-1].strip()
                    date = sms_send[0].split(' ')[1]
                    time_drop = sms_send[0].split(' ')[3]
                    id_item = sms_send[3].split('[')[1].split(']')[0]
                    id_settings = id_item.split('-')
                    
                    quotes = soup.find('li', class_=f'q{id_settings[3]} i{id_settings[0]}')
                    name_drop = quotes.find('em').text

                    drop_sms = f"{name_account} получил  {name_drop}"
                    print(drop_sms)
                    bot.start()
                    bot.send_message(name_chat,drop_sms)
                    bot.disconnect()
                a = sum(1 for line in open(path_logs, 'r',encoding='utf-8'))

        except:
            pass          
    print("PARCER ЗАВЕРШИЛ РАБОТУ...")

Start()

