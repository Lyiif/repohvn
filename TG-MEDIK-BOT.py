import telebot
import ast
import time
from telebot import types

bot = telebot.TeleBot("5297534325:AAEzBIeJI7LLxs7CNnh5JVu25OdBPQbdGJE")
id_chat = 0
stringList1 = {"Name": "Украина", "Language": "Белорусь", "API": "Россия", "S": "Казахстан"}

stringList2 = {"Поиск медицинских услуг": "1", "Зарегистрироваться медику": "2", "Найти медика": "3", "Назад": "4"}

stringList3 = {"Дерматовенеролог": 5, "Гастроэнтеролог": 6, "Невролог": 7, "Психотерапевт": 8, "Психиатр": 9, "Гинеколог": 10, "Терапевт": 11, "Психолог": 12, "Дерматолог": 13, "Офтальмолог": 14, "Уролог": 15, "Трихолог": 16, "Кардиолог": 17, "Проктолог": 18, "Эндокринолог": 19, "Отоларинголог(ЛОР)": 20}

MsgIdToDelete = 0
def makeKeyboard():
    markup = types.InlineKeyboardMarkup()
    for key, value in stringList1.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "', '" + key + "']"),)
    return markup
def makeKeyboard2():
    markup = types.InlineKeyboardMarkup()
    for key, value in stringList2.items():
        markup.add(types.InlineKeyboardButton(text=key,
                                              callback_data="['value', '" + value + "']"),)
    return markup

def makeKeyboard3():
    markup = types.InlineKeyboardMarkup()
    i = 0
    for (key, value) in stringList3.items():
        markup.add(types.InlineKeyboardButton(text=list(stringList3.keys())[i],
                                              callback_data="['value', '" + str(list(stringList3.values())[i]) + "']"),
        types.InlineKeyboardButton(text=list(stringList3.keys())[i + 1],
                                              callback_data="['value', '" + str(list(stringList3.values())[i] + 1) + "']"),
        types.InlineKeyboardButton(text=list(stringList3.keys())[i + 2],
                                              callback_data="['value', '" + str(list(stringList3.values())[i] + 2) + "']"),
        types.InlineKeyboardButton(text=list(stringList3.keys())[i + 3],
                                              callback_data="['value', '" + str(list(stringList3.values())[i] + 3) + "']"))
        i += 4
        print(i)
        if i >= 16:
            return markup
            break

@bot.message_handler(commands=['start'])
def handle_command_adminwindow(message):
    global MsgIdToDelete
    MsgIdToDelete = bot.send_message(chat_id=message.chat.id,
                     text="Выберите страну",
                     reply_markup=makeKeyboard(),
                     parse_mode='HTML').id

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global MsgIdToDelete
    if (call.data.startswith("['value'")):
        print(f"call.data : {call.data} , type : {type(call.data)}")
        print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        bot.answer_callback_query(callback_query_id=call.id)
        try:
            bot.delete_message(call.message.chat.id, MsgIdToDelete)
        except Exception as e:
            print(e)
        if len(valueFromCallBack) < 3:

            if valueFromCallBack == "4":
                print("bruh so easy")
                MsgIdToDelete = bot.send_message(chat_id=call.message.chat.id,
                                 text="Выберите страну",
                                 reply_markup=makeKeyboard(),
                                 parse_mode='HTML').id

            if valueFromCallBack == "1":
                MsgIdToDelete = bot.send_message(chat_id=call.message.chat.id,
                                 text="Выберите врача",
                                 reply_markup=makeKeyboard3(),
                                 parse_mode='HTML').id

        else:
            MsgIdToDelete = bot.send_message(chat_id=call.message.chat.id,
                             text=f"Приветствую! Бот создан, чтобы Вы смогли быстро получить медицинскую помощь\nВаша страна - {valueFromCallBack}",
                             reply_markup=makeKeyboard2(),
                             parse_mode='HTML').id

while True:
    bot.polling(none_stop=True, interval=0, timeout=0)
