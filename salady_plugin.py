# -*- coding: utf-8 -*- 

import datetime
import json
import os
import re
import schedule
import time

from slackbot.bot import respond_to
from slackbot.bot import listen_to

from salady.menu import SaladyMenu
from salady.order import SaladyOrder

@respond_to(r'메뉴')
def show_menu(message):
	menu = SaladyMenu()

	attachments = [
		{
			"fallback": "Salady Menu - Saladys",
			"text": "<http://www.saladykorea.com/html/menu.php|Salady Menu>",				            
			"fields": [
				{
					"title": "Salady",
					"value": menu.show_saladys()
				}
			],
			"color": "#2D6CB5"
		},

		{
			"fallback": "Salady Menu - Main Toppings",
			"text": "<http://www.saladykorea.com/html/menu_03.php|Topping & Dressing>",				            
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

@respond_to('(.* \+)+ (.*)')
def order(message, items, item):
	item_list = items.split("+")
	item_list.append(item)
	
	name = message.channel._client.users[message.body['user']][u'name']
	salady, main_topping, sub_topping, dressing, size_up, price = SaladyOrder(name).order(item_list)
	attachments = make_order_attachment(salady, main_topping, sub_topping,
										dressing, size_up, price, "order")

	message.send_webapi(u"주문 내역은 다음과 같습니다.", json.dumps(attachments))

def make_order_attachment(salady, main_topping, sub_topping, 
						  dressing, size_up, price, state):
	if state == "order":
		msg = "전체 주문목록에 추가되었습니다."
	elif state == "show":
		msg = "잘못된 내역이 있으면 다시 주문해주세요!"

	attachments = [
		{
			"fallback": "Salady Order",
			"text": "",				            
			"fields": [
				{
					"title": salady + " 샐러디",
					"value": "( ): 기본 토핑"
				},
			],
			"color": "#333333"
		},
		{
			"fallback": "Salady Order - Topping",
			"text": "",				            
			"fields": [
				{
					"title": "Main Topping",
					"value": ", ".join(main_topping),
					"short": "true"
				},
				{
					"title": "Sub Topping",
					"value": ", ".join(sub_topping),
					"short": "true"
				}
			],
			"color": "#E54837"
		},
		{
			"fallback": "Salady Order - Option",
			"text": "",				            
			"fields": [
				{
					"title": "Dressing",
					"value": dressing,
					"short": "true"
				},
				{
					"title": "Size Up",
					"value": size_up,
					"short": "true"
				}
			],
			"color": "#ACD039"
		},
		{
			"fallback": "Salady Order - Price",
			"text": "",				            
			"fields": [
				{
					"title": "총 가격은 " + str(price) + "원 입니다.",
					"value": msg
				}
			]
		},
	]
	return attachments

@respond_to(r'주문목록')
def show_order_list(message):
	today = datetime.date.today()
	fname = today.isoformat() + ".json"

	try:
		with open(fname, 'r') as infile:
			order_dict = json.loads(infile.read())
			total_price = 0
			attachments = []
			index = 0
			color_list = ["#2D6CB5", "DCDCDC", "#ACD039", "#E54837", "#FFFF00"]
			for k,v in order_dict.items():
				name = k
				price = v["price"]
				total_price += int(price)
				summary = v["summary"]

				order_summary = {
					"fallback": "Salady Order",
					"text": "",				            
					"fields": [
						{
							"title": "@" + name + u" 님의 주문 내역입니다.",
							"value": summary,
							"short": "true"
						}
					],
					"color":color_list[index%5]
				}
				index += 1
				attachments.append(order_summary)
		total_price_summary = {
			"fallback": "Salady Order",
			"text": "",				            
			"fields": [
				{
					"title": "총 " + str(total_price) + "원 입니다.",
					"value": ""
				}
			],
			"color": "#333"
		}
		attachments.append(total_price_summary)

		message.send_webapi("", json.dumps(attachments))
#				total_price += price
#		total_price_msg = "총 가격은 " + str(total_price) + " 입니다."
#		message.send(total_price_msg) 
	except IOError as e:
		message.send("주문 내역이 없습니다! 주문해주세요.")

@listen_to(r'메튜')
def ban_matt1(message):
	message.send("Matthew 배신자..")

@listen_to(r'매튜')
def ban_matt2(message):
	message.send("배신자 Matthew!!!")

@listen_to(r'matt', re.IGNORECASE)
def ban_matt3(message):
	message.send("Matthew 배신자!!!")
