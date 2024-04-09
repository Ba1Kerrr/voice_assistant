import telebot;
from parce import search_price
bot = telebot.TeleBot('6434260055:AAE7JMZQZ45ijJAO2xYPChMnu3N35lhJ8Dk')
@bot.message_handler(commands=['start','help'])
def basic_2(message):
    bot.send_message(message.from_user.id, "Привет , Я бот для обмена криптовалютой.Я могу обменивать bitcoin и ethereum, если ты хочешь начать  обменивать валюту - просто напиши ее название")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ("Привет","привет"):
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Bitcoin":
        bot.send_message(message.from_user.id,search_price)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)