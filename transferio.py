from random import randint
import math
import telebot
import time
import webbrowser

epic = False
creating = False
bot = telebot.TeleBot('1942175353:AAHeQexDytXvxi7H9fFPAPKfF7RGHg-_is0')
print("m?")

#bot.send_message(message.chat.id, )


@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):

        try:
          webbrowser.get('windows-default').open(message.text)
          return None
        except Exception as e:
          print(e)

bot.polling(none_stop=True)
