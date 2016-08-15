#coding: UTF-8

import re
import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to

from salady.menu import SaladyMenu
from salady.order import SaladyOrder

@respond_to(r'메뉴')
def show_menu(message):
	menu = SaladyMenu()

	attachments = [
		{
			"fallback": "Salady Menu - Main Toppings",
			"text": "<http://www.saladykorea.com/html/menu_03.php|Salady Menu> - Topping & Dressing",				            
			"fields": [
				{
					"title": "Main Topping",
					"value": menu.show_main_toppings()
				}
			],
			"color": "#438C56"
		},
		{
			"fallback": "Salady Menu - Sub Toppings",
			"text": "",				            
			"fields": [
				{
					"title": "Sub Topping",
					"value": menu.show_sub_toppings()
				}
			],
			"color": "#E54837"
		},
		{
			"fallback": "Salady Menu - Dressings",
			"text": "",				            
			"fields": [
				{
					"title": "Dressing",
					"value": "전부 다 700원. \n" + menu.show_dressings()
				}
			],
			"color": "#ACD039"
		}

	]

	message.send_webapi(u"안녕하세요!  메뉴판 보여드릴께요.", json.dumps(attachments))

@respond_to('(.* \+)* (.*)')
def order(message, items, item):
	item_list = items.split("+")
	item_list.append(item)
	
	order = SaladyOrder().order(item_list)
	message.reply(order + " 맞으시죠?")


