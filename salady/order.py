# -*- coding: utf-8 -*- 

import datetime
import json
import os

from salady.menu import SaladyMenu
from salady.translate import SaladyTranslator

class SaladyOrder(object):

	def __init__(self, name):
		self.name = name

	def order(self, item_list):
		menu = SaladyMenu()
		translator = SaladyTranslator() 

		salady_kor = item_list[0].replace(" ", "")
		salady_eng = translator.lang_ko2en(salady_kor)
		del item_list[0]
		main, sub, dressing, price = menu.get_salady(salady_eng) 

		main_topping_kor = []
		main_topping_eng = []
		sub_topping_kor = []
		sub_topping_eng = []

		dressing_kor = translator.lang_en2ko(dressing)
		dressing_eng = dressing
		size_up = False

		for item_kor in item_list:
			item_eng = translator.lang_ko2en(item_kor.replace(" ",""))
			category = menu.item_2_category(item_eng)
			if category == "main":
				main_topping_kor.append(item_kor)
				main_topping_eng.append(item_eng)
			elif category == "sub":
				sub_topping_kor.append(item_kor)
				sub_topping_eng.append(item_eng)
			elif category == "dressing":
				dressing_kor = item_kor
				dressing_eng = item_eng
			elif category == "size_up":
				size_up = True
		
		if dressing_kor != "":
			dressing_kor = dressing_kor + "드래싱"
		else:
			dressing_kor = "드래싱: X"

		if size_up:
			size_up_str = "O"
		else:
			size_up_str = "X"

		price += self.calculate_total_price(salady_eng, main_topping_eng, sub_topping_eng,
											dressing_eng, size_up)

		summary = (salady_kor + "샐러디 \n" + 
				   ",".join(main_topping_kor) + " + " + ",".join(sub_topping_kor) + "\n" + 
				   dressing_kor + " , " + "사이즈업: " + size_up_str + "  \n " + 
				   " 가격: " + str(price))
		self.append_order_list(main_topping_eng, sub_topping_eng, 
							   dressing_eng, size_up, price, summary)
		
		basic_main = list(map(lambda x: "("+translator.lang_en2ko(x)+")", main))
		basic_sub = list(map(lambda x: "("+translator.lang_en2ko(x)+")", sub))

		return salady_kor, (basic_main + main_topping_kor), (basic_sub + sub_topping_kor), dressing_kor, size_up_str, price

	def calculate_total_price(self, salady, main_topping, 
							  sub_topping, dressing, size_up):
		menu = SaladyMenu()
		price = 0

		for main in main_topping:
			price += int(menu.get_price(main))
		for sub in sub_topping:
			price += int(menu.get_price(sub))
		if (salady == "my") and (dressing != ""):
			price += 700
		if size_up:
			price += 900
		return price

	def append_order_list(self, main_topping, sub_topping, 
						  dressing, size_up, price, summary):
		today = datetime.date.today()
		fname = today.isoformat() + ".json"

		name = self.name
		order = {
			"main_topping":main_topping,
			"sub_topping":sub_topping,
			"dressing":dressing,
			"size_up":size_up,
			"price":price,
			"summary":summary
		}

		if (os.path.isfile(fname)):
			order_dict = self.read_file(fname)
			if name in order_dict:
				order_dict.pop(name, None)
			order_dict[name] = order
		else:
			order_dict = {}
			order_dict[name] = order
		self.write_file(fname, order_dict)

	def read_file(self, fname):
		with open(fname, 'r') as infile:
			return json.loads(infile.read())

	def write_file(self, fname, data):
		with open(fname, 'w') as outfile:
			json.dump(data, outfile)

