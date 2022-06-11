#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
from random import randint
import math
import telebot
import re
import os
import time
import traceback
from datetime import datetime
import json
import pickle
from bs4 import BeautifulSoup
import requests, json
from googletrans import Translator
from pprint import pprint
import sys


print("Hello world !") # this is should be saved in yourlogfilename.txt

trans = Translator()
try:
    with open("krit.txt", "r") as f:
        krit = f.read().replace('\n', '')
    with open("miss.txt", "r") as f:
        miss = f.read().replace('\n', '')
    with open("trauma.txt", "r") as f:
        trauma = f.read().replace('\n', '|')
except:
    pass
####################################e7e090c39f51a21c944fad80af38ca56

####################################
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
headers = {

    'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

result = ""
def weather():
    global result
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Vienna"
    API_KEY = "bc99cf07dd88bff458d3195377ec7215"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       veterd = data["wind"]
       veter = veterd['speed']
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
       report = trans.translate(report[0]['description'], dest="ru").text
    else:
       # showing the error message
       print("Error in the HTTP request", URL)
    result = "Фэнтези погода!" + "\n" + "Сейчас в вашем районе Фаэруна " + report.lower() + ", " + str(int(temperature) - 273) + "°C" + "\n"+ "Скорость ветра - " + str(veter) + " миль/час" + "\n" + "Приключения.. всё впереди!"
    result = trans.translate(result, dest="ru").text
    print(URL)




#total = trans.translate(result, dest="ru")
#print(total.text)
print("Приключения.. всё впереди!")
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return str(o)

        return json.JSONEncoder.default(self, o)
print(datetime.now())
creating = False
bot = telebot.TeleBot('1910723121:AAHO8d5YNq-wGJImA2myoPWokORBkPsPYi4')

print("sssss")
dicenum  = 0
dicemast = 0
targetnum = 0
creating = False
name = ""
мм = 0
см = 0
зм = 0
эм = 0
пм = 0
godlist = ["ао", "аббатору","азуту","акади","амберли","темпусу","бейну","грумбару","истишие","келемвору","коссуту","латандеру","ллос","мистре","огме","сирику","сунэ","сильванусу","талосу","тиру","убтао","чаунтие","шар",
"бешабе","гонду","илматеру","миеликки","селюн","тиморе","умберли","хельму","денеиру","лиире","ловиатару","малару","маску","милилу","аурил","талоне","тиамат","торму","уокин","шондакулу","элдат","валькуру","вельшаруну","гарагосу","гарготу","гуэрону","джергалу","луруэ","нобаниону","саврасу",
"сиаморф","улутиу","утгару","химу", "финдеру","хоару","шаресс","шиаллии","миркулу","баалу"]
print(len(godlist))
with open(f"{os.getcwd()}/pouch.txt", 'r', encoding='utf-8') as f: #f"{os.getcwd()}\slova.txt"

    pouch = f.read()
    мм = int(pouch.split(" ")[0])
    см = int(pouch.split(" ")[1])
    зм = int(pouch.split(" ")[2])
    эм = int(pouch.split(" ")[3])
    пм = int(pouch.split(" ")[4])
    print(pouch)
    f.close()
#bot.send_message(message.chat.id, )
print(мм)
coins = 1000
prayers = []
try:
    with open("data.pickle", "rb") as f:
       prayers = pickle.load(f)
       print(f'holy people: {prayers}')

except:
    print("no data in prayers file mb", traceback.format_exc())
@bot.message_handler(content_types=['text'])




@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    print(message.from_user.id)
    global creating
    global prayers

    global мм
    global см
    global зм
    global эм
    global пм
    global coins
    global dx1
    global dx2
    global xd1
    global xd2
    global ac2
    global ac1
    global hp2
    global hp1
    global bonus1
    global bonus2
    global w1, w2

    xed = None

    try:
        if "бот,"in message.text.lower() and "крит" in message.text.lower():
            num = randint(1, 100)
            kritind = krit.find(str(num))
            endpoint = krit.find(".", kritind, -1)
            output = krit[kritind:endpoint].replace('\\n ', '\n').replace('\\t', '\t')
            print(output)
            xed = bot.send_message(message.chat.id,output)
            if randint(1, 20) == 1:
                num = randint(1, 20)
                traumind = trauma.find(str(num) + ")")
                endpoint = trauma.find("|", traumind, -1)
                output = trauma[traumind:endpoint].replace('\\n ', '\n').replace('\\t', '\t')
                print(output)
                xed = bot.send_message(message.chat.id,"Какая боль! Что то хрустнуло, соперник кричит от боли! Была нанесена травма! Это разрушит его жизнь \n" + output)
        if "бот,"in message.text.lower() and "промах" in message.text.lower():
            num = randint(1, 100)
            missind = miss.find(str(num))
            endpoint = miss.find(".", missind, -1)
            output = miss[missind:endpoint].replace('\\n ', '\n').replace('\\t', '\t')
            print(output)
            xed = bot.send_message(message.chat.id,output)
            if randint(1, 20) == 1:
                num = randint(1, 20)
                traumind = trauma.find(str(num) + ")")
                endpoint = trauma.find("|", traumind, -1)
                output = trauma[traumind:endpoint].replace('\\n ', '\n').replace('\\t', '\t')
                print(output)
                xed = bot.send_message(message.chat.id,"Ужасная боль... тело слабеет, получена травма.. лишь бы выжить.. \n" + output)
        if "бот," in message.text.lower() and "средн" in message.text.lower():
            entr = []
            xdx = message.text.lower().split(" ")[2]
            xd  = int(xdx.split("d")[0])
            dx = int(xdx.split("d")[1])
            i = 0
            number = 0
            for i in range(10000):
             for x in range(xd):
              number += randint(1, dx)
             entr.append(number)
             number = 0
            print(f"average for {xd}d{dx} is {sum(entr)/len(entr)}")
            xed = bot.send_message(message.chat.id, f"average for {xd}d{dx} is {sum(entr)/len(entr)}")

        if 'бот,' in message.text.lower() and  '>' in message.text.lower() and creating == False:
            try:
                dicenum  = int(message.text.lower().split(' ')[1].split("d")[0])
                dicemast = int(message.text.lower().split(' ')[1].split("d")[1])
                targetnum = int(message.text.lower().split(' ')[3])

                count = 0
                x = 10000
                succ = 0
                tryq = 0
                while count < x:
                    i = 0
                    tryq = 0
                    while i < dicenum:
                        tryq += randint(1, dicemast)
                        i += 1
                    if tryq >= targetnum:
                        succ += 1
                    count += 1
                print(f'шанс выкинуть на {dicenum}d{dicemast} число {targetnum} -', math.floor(succ / count * 100), '%')
                xed = bot.send_message(message.chat.id, f'шанс выкинуть на {dicenum}d{dicemast} число {targetnum} или больше составляет {math.floor(succ / count * 100)}%')
            except Exception:
                pass
        if 'бот,' in message.text.lower() and  '>' not in message.text.lower() and "d" in message.text.lower() and creating == False:
            try:
                dicenum  = int(message.text.lower().split(' ')[1].split("d")[0])
                dicemast = int(message.text.lower().split(' ')[1].split("d")[1])
                i = 0
                number = 0
                rvalues = []
                while i < dicenum:
                    rvalue = randint(1, dicemast)
                    number += rvalue
                    rvalues.append(rvalue)
                    i += 1
                print(f"{dicenum}d{dicemast} - {number} {rvalues}")

                xed = bot.send_message(message.chat.id, f"{dicenum}d{dicemast} - {number} {rvalues}")
            except Exception:
                pass
        if 'бот,' in message.text.lower() and 'кошел' in message.text.lower():
            bot.send_message(message.chat.id, f"В кошельке вот что:\n медных -                                {мм}\n серебрянных -                    {см}\n золотых -                          {зм}\n электрумовых -                  {эм}\n платиновых -                       {мм}\n в золотых это {int(мм / 100 + см / 10 + зм + эм * 5 + пм * 10)}, а в долларах - {int(мм / 100 + см / 10 + зм + эм * 5 + пм * 10) * 104}$")
        if 'бот,' in message.text.lower() and "сражение" not in message.text.lower() and "x" not in message.text.lower() and "х" not in message.text and ("+" in message.text.lower() or "-" in message.text.lower()):
            exec(message.text.split(" ")[1] + message.text.split(" ")[2] + "=" + message.text.split(" ")[3], globals())
            print(message.text.split(" ")[1] + message.text.split(" ")[2] + "=" + message.text.split(" ")[3])

            with open(f"{os.getcwd()}/pouch.txt", 'w', encoding='utf-8') as f: #f"{os.getcwd()}\slova.txt"
                f.write(f"{мм} {см} {зм} {эм} {пм}")
                xed = bot.send_message(message.chat.id, f"хорошо, теперь в кошельке вот что:\n медных -                                {мм}\n серебрянных -                    {см}\n золотых -                          {зм}\n электрумовых -                  {эм}\n платиновых -                       {мм}\n в золотых это {int(мм / 100 + см / 10 + зм + эм * 5 + пм * 10)}, а в долларах - {int(мм / 100 + см / 10 + зм + эм * 5 + пм * 10) * 104}$")
                #if message.text.split(" ")[2] == "+":
                    #gif = bot.send_message(message.chat.id, "https://media0.giphy.com/media/qoSbYdNydqcsI9h7JG/giphy.gif?cid=790b7611e13f2c44b530ce2b5bb7cb51c0719aebec2e3254&rid=giphy.gif&ct=g")
                    #time.sleep(4)
                    #bot.delete_message(message.chat.id, gif.message_id)
                f.close()
        if 'бот,' in message.text.lower() and 'расскажи про' in message.text.lower():
            searchword = message.text.split("расскажи про")[1]
            searchword = searchword.upper()
            searchword = searchword[1:]
            if len(searchword) > 3:
                searchword = searchword[:len(searchword)-1]

            pattern = f"{searchword}(.*?)/"

            print(f"searching from |{searchword}| to /")

            with open(f"{os.getcwd()}/slova.txt", 'r', encoding='utf-8') as f: #f"{os.getcwd()}\slova.txt"

                rules = f.read().replace('\n', "|")
                print(rules)
                try:
                    substring = re.search(pattern, rules).group(1)
                    substring = substring.replace('|', "\n")
                    substring = substring[1:]
                    xed = bot.send_message(message.chat.id, substring)
                    print(substring)
                except:
                    print("someone sent bullshit")
                    xed = bot.send_message(message.chat.id, f"че за.. не в курсе про {message.text.split('расскажи про')[1]}")
        if 'бот,' in message.text.lower() and 'статы' in message.text.lower():
            N = 4
            stats = []
            for i in range(6):
                a = []
                for i in range(N):
                    a.append(randint(1, 6))
                for i in range(N-1):
                    for j in range(N-i-1):
                        if a[j] > a[j+1]:
                            a[j], a[j+1] = a[j+1], a[j]
                print(a)
                stats.append(sum(a)-a[0])
            print(sum(stats))
            text = str(stats)
            if sum(stats) <= 60:
                text += "\nахахахахахах вот это статы хддд\nудачи выжить xDDD"
            if sum(stats) >= 82:
                text += "\n0_0 ого везучий челик"
            if sum(stats) < 82 and sum(stats) > 60:
                text += "\nну норм так, ничего выдающегося или слишком убогого"
            xed = bot.send_message(message.chat.id, text)
            print(text)
        if '⚽' in message.text.lower()  or "футбол" in message.text.lower() or "месси" in message.text.lower() or "динамо" in message.text.lower() or "роналдо" in message.text.lower():
            xed = bot.send_message(message.chat.id, "Проснулись футболисты🏳️‍🌈🏳️‍🌈🏳️‍🌈!! Поднять щиты!! 🛡🛡🛡🛡")
        if 'бот,' in message.text.lower() and 'сражение' in message.text.lower():
            hp1 = int(message.text.split("сражение ")[1][0])
            hp2 = int(message.text.split("и ")[1][0])
            print(hp1, hp2)
            ac1 = int(message.text.split(" кд")[0][-2:])
            ac2 = int(message.text.split("и ")[1].split(" кд")[0][-2:])
            print(ac1, ac2)
            bonus1 = int(message.text.split(" и ")[0].split("+")[1][0])
            bonus2 = int(message.text.split(" и ")[1].split("+")[1][0])
            print(bonus1, bonus2)
            xd1=int(message.text.split(" и ")[0].split("d")[0][-1])
            dx1=int(message.text.split(" и ")[0].split("d")[1][0])
            xd2=int(message.text.split(" и ")[1].split("d")[0][-1])
            dx2=int(message.text.split(" и ")[1].split("d")[1][0])
            w1 = 0
            w2 = 0
            class killed(Exception): pass
            def p1attack():
                global dx1
                global dx2
                global xd1
                global xd2
                global ac2
                global hp2
                global bonus1
                global w1, w2

                if randint(1, 20) + bonus1 >= ac2:
                    hp2 -= xd1 * randint(1, dx1)
                    #print("первый попал по второму")
                #else:
                    #print("первый не попал по второму")
                if hp2 <= 0:
                    #print("first won")
                    hp1 = int(message.text.split("сражение ")[1][0])
                    hp2 = int(message.text.split("и ")[1][0])
                    w1 += 1
                    #print("победа первого!!!!!!")
                    raise killed
            def p2attack():
                global dx1
                global dx2
                global xd1
                global xd2
                global ac1
                global hp1
                global bonus2
                global w1, w2
                if randint(1, 20) + bonus2 >= ac1:
                    hp1 -= xd2 * randint(1, dx2)
                    #print("второй попал по первому")
                #else:
                    #print("второй не попал по первому")
                if hp1 <= 0:
                    #print("second won")
                    hp1 = int(message.text.split("сражение ")[1][0])
                    hp2 = int(message.text.split("и ")[1][0])
                    w2 += 1
                    #print("победа второго!!!!!!!")
                    raise killed
            print(xd1, dx1,xd2, dx2)
            turn = randint(1,2)

            for i in range (1000):
                turn = randint(1,2)
                try:
                    while hp1 > 0 or hp2 > 0:
                        if turn == 1:
                            #print("первым ходит первый")
                            p1attack()
                            p2attack()

                        if turn == 2:
                            #print("первым ходит второй")
                            p2attack()
                            p1attack()
                except killed:
                    pass


            print(f"первый победил в {w1/10}% случаев, а второй - в {w2/10}%.")
            xed = bot.send_message(message.chat.id, f"первый победил в {w1/10}% случаев, а второй - в {w2/10}%.")
        if 'бот,' in message.text.lower() and 'рстки' in message.text.lower():
            betnum = int(message.text.split(' ')[2])
            betval = message.text.split(' ')[3]
            betpos = int(message.text.split(' ')[5])
            winpos = randint(1,3)
            winpos = randint(1,3)
            if betnum == 0:
                xed = bot.send_message(message.chat.id, "э")
                raise Exception
            exec(f"coins = {betval}-{str(betnum)}", globals())
            if coins < 0:
                print("poor!")
                xed = bot.send_message(message.chat.id,f"в долги войдете! у вас есть только {globals()[betval]} {betval}")
                raise Exception
            print("coins = "+str(coins))
            globals()[betval] -= betnum
            msgbase = "hehe, казиныч)\nтакс, посмотрим чё тут у нас:\n"
            msgtoedit = bot.send_message(message.chat.id,f"hehe, казиныч)\nтакс, посмотрим чё тут у нас:")
            xed = msgtoedit
            time.sleep(0.5)
            msgbase += "\n◇"
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            time.sleep(0.5)
            msgbase += "   ◇"
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            time.sleep(0.5)
            msgbase += "   ◇"
            print(len(msgbase)) # 46 47 48
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            time.sleep(0.5)
            msgbase =  "hehe, казиныч)\nтакс, посмотрим чё тут у нас:\n"
            msgbase += " " + " " * (betpos-1) * 7 +"⇓ ваш"
            msgbase += "\n◇   ◇   ◇"
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            time.sleep(0.5)
            msgbase += f"\nставка на {betpos} кубик...."
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            time.sleep(2)
            l = list(msgbase)
            l[-22 - 4 * (3-winpos)-1] = "◈"
            msgbase= ''.join(l)
            bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)

            print("winlose = ", winpos, betpos)
            if betpos == winpos:
                print("w", betpos)
                exec(f"{str(betval)}+={str(betnum*3)}")
                time.sleep(0.5)
                msgbase += f"\nОтлично! деньги ваши!\nВыигрыш:{betnum * 3} {betval}"
                bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            else:
                time.sleep(0.5)
                msgbase += f"\nПечально. Потерянные деньги!"
                bot.edit_message_text(msgbase, message.chat.id, msgtoedit.id)
            with open(f"{os.getcwd()}/pouch.txt", 'w', encoding='utf-8') as f: #f"{os.getcwd()}\slova.txt"
                f.write(f"{мм} {см} {зм} {эм} {пм}")
        if 'бот,' in message.text.lower() and 'молитва' in message.text.lower():
            def getDifference(then):
                now = datetime.now()
                duration = now - then
                duration_in_s = duration.total_seconds()

                #Date and Time constants
                hour_ct = 60 * 60 	    #3600

                def hrs():
                  return divmod(duration_in_s, hour_ct)[0]

                return int(hrs())


            loyalty = 0
            relig = 2
            if message.text.split(' ')[2].lower() in godlist:

                if message.from_user.id not in [i[0] for i in prayers]:
                  loyalty = int(randint(0, 5) * (godlist.index(message.text.split(' ')[2]).lower() / 21))
                  elem = message.from_user.id, message.text.split(' ')[2], loyalty, datetime.now(), message.from_user.first_name
                  prayers.append(elem)
                  print(f"first   вы укрепили преданность {message.text.split(' ')[2]}. Теперь ваша преданность равна {loyalty}")
                  xed = bot.send_message(message.chat.id,f"Новое поклонение! Вы начали молиться {message.text.split(' ')[2].capitalize()}. Теперь ваша преданность равна {loyalty}")

                else:
                  print([i[0] for i in prayers])
                  for iteration, id in enumerate([i[0] for i in prayers]):
                      if id == message.from_user.id:
                          ind = iteration
                      else:
                          print(f"{id} != {message.from_user.id}")

                  if getDifference(prayers[ind][3]) >= 6 or "hvn" in message.text:
                      rseed = randint(0,5)
                      oldloy = prayers[ind][2]
                      loyalty = int(rseed * (godlist.index(message.text.split(' ')[2].lower()) / 21)) + prayers[ind][2]
                      if loyalty == prayers[ind][2]:
                          loyalty += 1
                      elem = message.from_user.id, message.text.split(' ')[2].lower(), loyalty, datetime.now(), message.from_user.first_name
                      prayers[ind] = elem
                      print(f"вы укрепили преданность {message.text.split(' ')[2]}. Теперь ваша преданность равна {loyalty}")
                      print("rolled ", rseed, "multiplied by ", (godlist.index(message.text.split(' ')[2].lower()) / 21), " =",{int(rseed * (godlist.index(message.text.split(' ')[2].lower()) / 21))}, "then - ", {oldloy}, "now - ", {loyalty})
                      xed = bot.send_message(message.chat.id,f"Вы укрепили преданность {message.text.split(' ')[2].capitalize()}. Теперь ваша преданность равна {loyalty}")
                  else:
                      xed = bot.send_message(message.chat.id,f"Вы молились {getDifference(prayers[ind][3])} часов назад. Молиться можно не чаще чем раз в 6 часов. не вежливо!")
                strprayers = prayers
                print("!!!!!!!!!!!!!", strprayers)
                for i in strprayers:
                    i = list(i)
                    i[3] = str(i[3])
                    menace = tuple(i)
                    i = menace
                for i in menace:
                    print(type(i))
                with open('data.pickle', 'wb') as f:
                    pickle.dump(strprayers, f)
        if 'бот,' in message.text.lower() and 'погода' in message.text.lower():
            weather()
            total = trans.translate(result, dest="ru")
            print(total.text)
            xed = bot.send_message(message.chat.id, total.text)
        if 'бот,' in message.text.lower() and 'йсоветй' in message.text.lower():
            priest=""
            kanzler = ""
            uprav = ""
            marshal = ""
            spy = ""
            council = [priest, kanzler, uprav, marshal, spy]
            uprtxt = open('uprav_task_events.txt', 'r')
            upr = uprtxt.readlines()
            pritxt = open('priest_task_events.txt', 'r')
            pri = pritxt.readlines()
            spytxt = open('spymaster_task_events.txt', 'r')
            spy = spytxt.readlines()
            kantxt = open('kanzler_task_events.txt', 'r')
            kan = kantxt.readlines()
            martxt = open('marshal_task_events.txt', 'r')
            mar = martxt.readlines()
            txtcounc = [pri, kan, upr, mar, spy]
            for i, chel in enumerate(council):
            	if random.randint(1, 10) == 10:
            		council[i] = random.choice(txtcounc[council.index(chel)])
            		print("tried randint")
            	elif random.randint(1, 50) == 1:
            	    print("dead")
            	    council[i] = "dead"
            	else:
            	    council[i] = "alive"
            print(council)
            xed = bot.send_message(message.chat.id,f"священник - {council[0]},\nканцлер - {council[1]},\nуправляющий - {council[2]},\nмаршал - {council[3]},\nтайный советник - {council[4]}")
        if 'бот,' in message.text.lower() and 'донжон' in message.text.lower():
            xed = bot.send_message(message.chat.id,f"https://donjon.bin.sh")
        if "бот," in message.text.lower() and "лог" in message.text.lower():
            log = open("log.txt", "rb")
            bot.send_document(message.chat.id, log)

    except Exception as e:
        print("THE FUCK ?", traceback.format_exc())
    except KeyboardInterrupt:
        sys.stdout.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    if 'бот,' in message.text.lower() and ("-x" in message.text or "-х" in message.text):
       time.sleep(4)
       bot.delete_message(message.chat.id, message.id)
       bot.delete_message(message.chat.id, xed.id)
@bot.message_handler(content_types=['dice'])
def get_stupid_messages(dicemess):
    print("recieved dice")
    if dicemess.dice.emoji == "⚽":
        bot.send_message(dicemess.chat.id,"Проснулись футболисты🏳️‍🌈🏳️‍🌈🏳️‍🌈!! Поднять щиты!! 🛡🛡🛡🛡")

bot.infinity_polling()
