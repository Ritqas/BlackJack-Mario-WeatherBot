import telebot

import random

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("камень")
    keyboard.row("ножницы")
    keyboard.row("бумага")


@bot.message_handler(content_types=['text'])
def text(message):
    spisok_hod = ["камень", "ножницы", "бумага"]
    y = (random.choice(spisok_hod))
    bot.send_message(message.chat.id, y)
    if message.text == "ножницы":
        if y == "бумага":
            bot.send_message(message.chat.id, "вы победили")
        else:
            if y == "камень":
                bot.send_message(message.chat.id, "вы проиграли")
            else:
                if y == "ножницы":
                    bot.send_message(message.chat.id, "ничьия")
    if message.text == "бумага":
        if y == "камень":
            bot.send_message(message.chat.id, "вы победили")
        else:
            if y == "ножницы":
                bot.send_message(message.chat.id, "вы проиграли")
            else:
                if y == "бумага":
                    bot.send_message(message.chat.id, "ничьия")
    if message.text == "камень":
        if y == "камень":
            bot.send_message(message.chat.id, "ничия")
        else:
            if y == "ножницы":
                bot.send_message(message.chat.id, "вы победили")
            else:
                if y == "бумага":
                    bot.send_message(message.chat.id, "вы проиграли")


bot.polling(none_stop=True)