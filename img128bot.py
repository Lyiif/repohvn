import telebot
import re
from telebot import types as ttypes
from fastbook import *

import traceback
import json
from time import sleep
def geturl(word):
    urls = search_images_ddg(word, max_images=24)
    return urls[0:23]


bot = telebot.TeleBot('2138193170:AAF2qnQoEdlGr-acEtUN4cHG09WBZdiNCvk')
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
	try:
		urls = geturl(query.query)
		print(dir(types))
		results = [
			ttypes.InlineQueryResultPhoto(
			   	id='1',
				title=query.query,
				photo_url = urls[1],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[1]),

			ttypes.InlineQueryResultPhoto(
			   	id='2',
				title=query.query,
				photo_url = urls[2],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[2]),

			ttypes.InlineQueryResultPhoto(
			   	id='3',
				title=query.query,
				photo_url = urls[3],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[3]),

			ttypes.InlineQueryResultPhoto(
			   	id='4',
				title=query.query,
				photo_url = urls[4],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[4]),
			ttypes.InlineQueryResultPhoto(
			   	id='5',
				title=query.query,
				photo_url = urls[5],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[5]),

			ttypes.InlineQueryResultPhoto(
			   	id='6',
				title=query.query,
				photo_url = urls[6],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[6]),

			ttypes.InlineQueryResultPhoto(
			   	id='7',
				title=query.query,
				photo_url = urls[7],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[7]),

			ttypes.InlineQueryResultPhoto(
			   	id='9',
				title=query.query,
				photo_url = urls[9],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[9]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='10',
				title=query.query,
				photo_url = urls[10],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[10]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='11',
				title=query.query,
				photo_url = urls[11],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[11]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='12',
				title=query.query,
				photo_url = urls[12],
				photo_width = 8,
				photo_height = 8,
			thumb_url = urls[12]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='13',
				title=query.query,
				photo_url = urls[13],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[13]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='14',
				title=query.query,
				photo_url = urls[14],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[14]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='15',
				title=query.query,
				photo_url = urls[15],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[15]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='16',
				title=query.query,
				photo_url = urls[16],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[16]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='17',
				title=query.query,
				photo_url = urls[17],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[17]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='18',
				title=query.query,
				photo_url = urls[18],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[18]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='19',
				title=query.query,
				photo_url = urls[19],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[19]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='20',
				title=query.query,
				photo_url = urls[20],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[20]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='21',
				title=query.query,
				photo_url = urls[21],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[21]),
            
            ttypes.InlineQueryResultPhoto(
			   	id='22',
				title=query.query,
				photo_url = urls[22],
				photo_width = 8,
				photo_height = 8,
				thumb_url = urls[22]),

			]

		bot.answer_inline_query(query.id, results)
		sleep(1)
	except Exception as e:
		print(traceback.format_exc())
bot.infinity_polling()
