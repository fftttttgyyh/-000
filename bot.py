# bot.py
import telebot
import os

TOKEN = os.getenv("8069895630:AAH0Bm9HUiNgI5kYTDvuF4xAtNyxpLzxIf0")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я работаю на Zeabur 🎉")

bot.polling()
