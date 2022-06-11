from threading import Timer
import telebot

bot = telebot.TeleBot('5280010070:AAGPu8VI0QSlO3RQdNgKUHVg6_cPq_McYVo')
@bot.message_handler(content_types=['text'])
def getmes(message):
  def s(word):
    bot.send_message(message.chat.id, word.split("=")[0]+ " ||" + word.split("=")[1] + "||", parse_mode="MarkdownV2")
  try:
      Timer(3600, s, [message.text]).start()
      Timer(3600*24, s, [message.text]).start()
      Timer(3600*24*7, s, [message.text]).start()
  except Exception as e:
      print(traceback.format_exc())
bot.infinity_polling() 