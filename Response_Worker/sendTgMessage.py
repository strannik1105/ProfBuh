import telebot
from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, спасибо за использование сервиса!\nКак будет готова статья, я отправлю вам ссылку")
    bot.send_message(message.chat.id, message.chat.id)

def send_url(userId, URL):
    bot.send_message(userId, f"Статья готова, ссылка на скачивание: P{URL}")

bot.infinity_polling()

