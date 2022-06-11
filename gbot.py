import telebot
import re
from telebot import types
import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import time
import traceback
import json
from time import sleep
import threading
from selenium import webdriver
from requests import Session, Request
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
zaprosiks = 0
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())
busy = False
prev_id = 0
def geturl(word):
	global prev_id
	global busy
	busy = True
	global zaprosiks
	headers = {
		"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
	}
	params = {
		"q": word,
		"tbm": "isch",
		"hl": "en",
		"ijn": "0",
	}
	r = requests.Request('POST',"https://www.google.com/search", params=params)
	prep = r.prepare()
	print(prep.url)

	browser.get(prep.url)
	#time.sleep(1)
	html = browser.page_source
	soup = BeautifulSoup(html, 'lxml')
	#print(html.text)
	all_script_tags = soup.select('script')

	matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

	matched_images_data_fix = json.dumps(matched_images_data)
	matched_images_data_json = json.loads(matched_images_data_fix)

	matched_google_image_data = re.findall(r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",', matched_images_data_json)

	matched_google_images_thumbnails = ', '.join(
		re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
				   str(matched_google_image_data))).split(', ')

	for fixed_google_image_thumbnail in matched_google_images_thumbnails:
		google_image_thumbnail_not_fixed = bytes(fixed_google_image_thumbnail, 'ascii').decode('unicode-escape')
	removed_matched_google_images_thumbnails = re.sub(
		r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '', str(matched_google_image_data))

	matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
													   removed_matched_google_images_thumbnails)

	print('\nku, chekayu slovo', word)  # in order
	zaprosiks += 1
	urls = []
	for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
		original_size_img_not_fixed = bytes(fixed_full_res_image, 'ascii').decode('unicode-escape')
		original_size_img = bytes(original_size_img_not_fixed, 'ascii').decode('unicode-escape')
		opener=urllib.request.build_opener()
		opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
		urls.append(original_size_img)
	print(urls[0:12])
	return urls[0:12]

bot = telebot.TeleBot('2138193170:AAF2qnQoEdlGr-acEtUN4cHG09WBZdiNCvk')
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
	global prev_id
	global busy
	try:
		print(busy, 'is busy, here am i!')
		if busy == False and query.query[-1] == ".":
			print("called!")
			urls = geturl(query.query)
			results = [
				types.InlineQueryResultPhoto(
				   	id='1',
					title=query.query,
					photo_url = urls[1-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[1-1]),

				types.InlineQueryResultPhoto(
				   	id='2',
					title=query.query,
					photo_url = urls[2-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[2-1]),

				types.InlineQueryResultPhoto(
				   	id='3',
					title=query.query,
					photo_url = urls[3-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[3-1]),

				types.InlineQueryResultPhoto(
				   	id='4',
					title=query.query,
					photo_url = urls[4-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[4-1]),
				types.InlineQueryResultPhoto(
				   	id='5',
					title=query.query,
					photo_url = urls[5-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[5-1]),

				types.InlineQueryResultPhoto(
				   	id='6',
					title=query.query,
					photo_url = urls[6-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[6-1]),

				types.InlineQueryResultPhoto(
				   	id='7',
					title=query.query,
					photo_url = urls[7-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[7-1]),

				types.InlineQueryResultPhoto(
				   	id='8',
					title=query.query,
					photo_url = urls[8-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[8-1]),

				types.InlineQueryResultPhoto(
				   	id='9',
					title=query.query,
					photo_url = urls[9-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[9-1]),

				types.InlineQueryResultPhoto(
				   	id='10',
					title=query.query,
					photo_url = urls[10-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[10-1]),

				types.InlineQueryResultPhoto(
				   	id='11',
					title=query.query,
					photo_url = urls[11-1],
					photo_width = 8,
					photo_height = 8,
					thumb_url = urls[11-1]),

				types.InlineQueryResultPhoto(
				   	id='12',
					title=query.query,
					photo_url = 'https://cpng.pikpng.com/pngl/s/178-1787846_my-pixel-arts-pixel-heart-break-clipart.png',
					photo_width = 8,
					photo_height = 8,
					input_message_content =types.InputTextMessageContent(message_text="Если вам пришелся этот бот по душе,\nто можете отблагодарить создателя,\nиспользуя следующие реквизиты:\nbtc: bc1qs2jlzh28stw45v6fj9777zuy2u4jnf8mum3xlm\neth: 0x2DCa93F4b5D6F3E1083055BC2057359c289ae338\nxrp: rUn4fV8bBn1dn6Z9VdjgSrdogMqDyAezM5\nс любовью, overheaven\n<3"),
					thumb_url = 'https://cpng.pikpng.com/pngl/s/178-1787846_my-pixel-arts-pixel-heart-break-clipart.png'),
				]

			bot.answer_inline_query(query.id, results)
			prev_id = query.from_user.id
			busy = False
			#sleep(1)
		else:
			print("busy")
	except Exception as e:
		print(traceback.format_exc())
		busy = False
def report():
	global zaprosiks
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	if current_time >= "22:30:00":#23:00:00
		bot.send_message(518029165, f"воззваний к бот(г)у сегодня - {zaprosiks}" )
		zaprosiks = 0
		timer = threading.Timer(7200.0, report)
		timer.start()
	else:
		timer = threading.Timer(60.0, report)
		timer.start()
report()
bot.infinity_polling()
