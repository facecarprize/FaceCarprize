# facecar_bot_env.py
import telebot
import random
import os
from dotenv import load_dotenv

from facecar_phrases_REAL_FULL_900 import STARTERS, MIDDLES, ENDINGS

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я FaceCar-бот. Напиши /пост — получишь готовый текст.")

@bot.message_handler(commands=['пост'])
def generate_post(message):
    post = f"{random.choice(STARTERS)} {random.choice(MIDDLES)} {random.choice(ENDINGS)}"
    bot.send_message(message.chat.id, post)

if __name__ == "__main__":
    bot.polling(none_stop=True)
