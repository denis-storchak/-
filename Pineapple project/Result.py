codes = dict()
names = []
all_ids = []
read_ids = []
missing_ids = []
info = ''

def reader():
    global info

    codes = dict()
    names = []
    all_ids = []
    read_ids = []
    missing_ids = []

    #получаем входной файл с номерами присутствующих
    with open('user_ids.txt', 'r') as f:
        for line in f:
            read_ids.append(line.strip())
            read_ids = set(read_ids)
            #print(read_ids)

    #print()


    #считываем в память эталонный список имен
    with open('codenames.txt', 'r') as f:
        for line in f:
            a = line.split()
            us_id, us_name = a[0], a[1:]
            codes[us_id] = us_name
            all_ids.append(us_id)
            #print(all_ids)

    #print()
    missing_ids = []

    #проверяем, кого нет
    for us_id in all_ids:
        if us_id not in read_ids:
            missing_ids.append(us_id)
        #print(missing_ids)

    info = 'Отсутствуют:\n'

    #пилим строку с именами отсутствующих
    for us_id in missing_ids:
        info += codes[us_id][0] + ' ' + codes[us_id][2] + ' ' + codes[us_id][3] + '\n'

    if len(missing_ids) == 0:
        info = 'Все на месте'

    #print(missing_ids)
    time.sleep(2)



def call():
    with open('user_ids.txt', 'w') as f:
        f.write('')
        
        


#пилим бота

# -*- coding: utf-8 -*-
import telebot
import logging
import colorlog
import emoji
import time
import datetime
from threading import Thread

TOKEN = "414949195:AAHm63cNUdHrSOjKgKdOC4LUK0L8xAzFxI8"

bot = telebot.TeleBot(TOKEN)

#бот в ответ на команду выдает список отсутствующих
@bot.message_handler(commands = ['info'])
def send_msg(message):
    reader()
    #keyboard = types.KeyboardMarkup()
    #url_button = types.KeyboardButton(text="Начать новое мероприятие", callback = call())
    #keyboard.add(url_button)
    msg = bot.send_message(message.chat.id, info)

@bot.message_handler(commands = ['new'])
def send_msg(message):
    call()
    msg = bot.send_message(message.chat.id, 'Новое мероприятие успешно начато!')

bot.polling(none_stop = True)
