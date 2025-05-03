
import telebot
import os
import random
import time

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

STARTERS = [
    "Очередной день — очередной салон в труху.",
    "Смотрим на этот потолок и понимаем: это будет надолго.",
    "Утро началось с химчистки, и, походу, это надолго.",
]

MIDDLES = [
    "Такой срач, будто тут ночевал табор.",
    "Ковры — как асфальт после зимы: всё в крошку и грязи.",
    "Запах в салоне такой, что даже мойка боится включаться.",
]

ENDINGS = [
    "Но ничего, вытащим, сделаем, будет как с витрины.",
    "Уже в процессе — скоро покажем результат.",
    "На связи FaceCar — спасаем интерьер с нуля.",
]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я FaceCar-бот. Напиши /post — получишь готовый текст.')

@bot.message_handler(commands=['post'])
def send_post(message):
    post = f"{random.choice(STARTERS)} {random.choice(MIDDLES)} {random.choice(ENDINGS)}"
    bot.send_message(message.chat.id, post)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(5)
