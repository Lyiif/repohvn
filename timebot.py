from datetime import datetime, timedelta
import telebot
bot = telebot.TeleBot('5277402524:AAE68ErKwLsgf3w9QOECn_mH4AHzrBrwqK0')

def geta(string):
    global xdate
    xdate= datetime.strptime(string, "%m/%d/%Y %I:%M %p")
    xdate += timedelta(hours=7, minutes=0)
    mydate = datetime.now()
    return str(xdate-mydate)[:-7]
@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):

    bot.send_message(message.chat.id, "начало через "+geta(message.text)+" в "+str(xdate))
bot.infinity_polling()
