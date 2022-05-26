import telebot
import os

bot = telebot.TeleBot(os.environ.get("API_KEY"))


@bot.message_handler(commands=["ping"])
def get_ping(message):
    bot.reply_to(message, f"Bot listening => {message.date}")


@bot.message_handler(commands=["message"])
def get_mesage(message):
    bot.send_message(message.chat.id, f"Bot listening => {message.date}")


print('Bot listening...')
bot.polling()
