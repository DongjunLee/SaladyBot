# -*- coding: utf-8 -*- 

from salady.translate import SaladyTranslator

class SaladyMenu(object):
	
	def __init__(self):
		self.saladys = self.__salady_meus()
		self.main_toppings = self.__main_topping()
		self.sub_toppings = self.__sub_topping()
		self.dressings = self.__dressings()
	
	def show_saladys(self):
		menu_str = ""
		translator = SaladyTranslator()
		for item in self.saladys.keys():
			menu_str += "| " + translator.lang_en2ko(item) + " 샐러디 | "
			main, sub, dressing, price = self.saladys[item]
			
			main = list(map(lambda x: translator.lang_en2ko(x), main))
			sub = list(map(lambda x: translator.lang_en2ko(x), sub))
			dressing = translator.lang_en2ko(dressing)		

			menu_str += (", ".join(main) + ", " + ", ".join(sub) + " " + 
						 dressing + " 드래싱  가격 : " + str(price) + "\n")
		return menu_str
		
	def show_main_toppings(self):
		menu_str = "| "
		item_index = 0
		translator = SaladyTranslator()
		for item in self.main_toppings.keys():
			menu_str += translator.lang_en2ko(item) + ": " + str(self.get_price(item)) + " | "
			item_index += 1
			if (item_index % 3 == 0) and (item_index % 9 != 0):
				menu_str += "\n | "
		return menu_str

	def show_sub_toppings(self):
		menu_str = "| "
		item_index = 0
		translator = SaladyTranslator()
		for item in self.sub_toppings.keys():
			menu_str += translator.lang_en2ko(item) + ": " + str(self.get_price(item)) + " | "
			item_index += 1
			if item_index % 4 == 0:
				menu_str += "\n | "
		return menu_str

	def show_dressings(self):
		menu_str = "| "
		item_index = 0
		translator = SaladyTranslator()
		for item in self.dressings.keys():
			menu_str += translator.lang_en2ko(item) + " | "
			item_index += 1
			if item_index % 3 == 0:
				menu_str += "\n | "
		return menu_str

	def get_price(self, item):
		if item in self.main_toppings:
			return self.main_toppings[item]
		elif item in self.sub_toppings:
			return self.sub_toppings[item]
		elif item in self.dressings:
			return 700
		return 'not exist price value' + item

	def get_explain(self, item):
		if item in self.dressings:
			return self.dressings[item]
		return 'not exist explain value' + item

	def __main_topping(self):
		main_toppings = {
			'chicken':1200,
			'sweet potato':1200,
			'egg':600,
			'tofu':800,
			'bacon':800,
			'ground beef':1000,
			'salmon':2000,
			'fruit cheese':1300,
			'green grapes':1200,
		}
		return main_toppings

	def __sub_topping(self):
		sub_toppings = {
			'cranberry':500,
			'kidney bean':500,
			'corn':500,
			'tortilla chip':500,
			'baked bean':500,
			'onion':500,
			'shredded cheese':800,
			'nuts':800,
			'tomato':600,
			'olve':600
		}
		return sub_toppings	

	def __dressings(self):
		dressings = {
			'caesar': u"크리미하고 담백한 맛의 샐러디의 대표적인 드레싱",
			'honey mustard': u"머스터드 소스에 꿀을 첨가한 달콤한 드레싱",
			'oriental': u"간장으로 만든 고소하고 깔끔한 맛의 드레싱",
			'creamy chilly': u"칠리소스로 매콤한 맛을 낸 드레싱",
			'lemon': u"레몬의 상큼한 향이 느껴지는 과일 드레싱",
			'balsamic': u"올리브 오일에 발사믹 식초를 섞은 새콤달콤한 드레싱",
			'citron': u"유자청을 갈아 만든 달콤한 드레싱",
			'basil pesto': u"신선한 바질과 잣이 들어간 향긋한 드레싱"
		}
		return dressings

	def item_2_category(self, item):
		if item in self.main_toppings:
			return "main"
		elif item in self.sub_toppings:
			return "sub"
		elif item in self.dressings:
			return "dressing"
		elif item == "size_up":
			return "size_up"
		else:
			return "not exist"

	def get_salady(self, item):
		return self.saladys[item]

	def __salady_meus(self):
		salady = {
			'chicken':self.chicken_salady(),
			'sweet':self.sweet_salady(),
			'egg':self.egg_salady(),
			'tofu':self.tofu_salady(),
			'mexican':self.mexican_salady(),
			'salmon':self.salmon_salady(),
			'triple cheese':self.triple_cheese_salady(),
			'classic':self.classic_salady(),
			'my':self.my_salady()
		}
		return salady

	def chicken_salady(self):
		main = ['chicken']
		sub = ['cranberry']
		dressing = "caesar"
		price = 5400
		return main, sub, dressing, price
	
	def sweet_salady(self):
		main = ['sweet potato']
		sub = ['kidney bean']
		dressing = "oriental"
		price = 5400
		return main, sub, dressing, price

	def egg_salady(self):
		main = ['egg']
		sub = ['corn']
		dressing = "honey mustard"
		price = 4800
		return main, sub, dressing, price

	def tofu_salady(self):
		main = ['tofu']
		sub = ['tomato']
		dressing = "oriental"
		price = 5000
		return main, sub, dressing, price

	def mexican_salady(self):
		main = ['ground beef', ]
		sub = ['baked bean', 'tortilla chip', 'sour cream']
		dressing = "creamy chilly"
		price = 5200
		return main, sub, dressing, price

	def salmon_salady(self):
		main = ['salmon']
		sub = ['onion']
		dressing = "lemon"
		price = 6200
		return main, sub, dressing, price

	def triple_cheese_salady(self):
		main = ['fruit cheese']
		sub = ['shredded cheese', 'parmesan cheese']
		dressing = "balsamic"
		price = 5800
		return main, sub, dressing, price

	def classic_salady(self):
		main = ['green grapes', ]
		sub = ['tomato', 'olve', 'nuts']
		dressing = "basil pesto"
		price = 5800
		return main, sub, dressing, price

	def my_salady(self):
		main = []
		sub = []
		dressing = ""
		price = 4100
		return main, sub, dressing, price

	def tandanji_salady(self):
		main = ['chicken', 'sweet potato']
		sub = ['kidney bean']
		dressing = "oriental"
		price = 6900
		return main, sub, dressing, price

