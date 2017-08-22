# -*- coding: utf-8 -*-
import telebot
import logging
import colorlog
import emoji
import time
import datetime

TOKEN = "414949195:AAHm63cNUdHrSOjKgKdOC4LUK0L8xAzFxI8"

bot = telebot.TeleBot(TOKEN)

info = ''
everyone = dict()

with open('codenames.txt', 'r') as f:
    for line in f:
        a = line.split()
        everyone[a[0]] = a[1:]

with open('missing_ids.txt', 'r') as f:
    for line in f:
        a = line.strip()
        info += ' '.join(everyone[a]) + '\n'

@bot.message_handler(commands = ['i'])
def send_msg(message):
    msg = bot.send_message(message.chat.id, info)

bot.polling(none_stop=True)
