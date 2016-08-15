#coding: UTF-8

class SaladyMenu(object):
	
	def __init__(self):
		self.main_toppings = self.__main_topping()
		self.sub_toppings = self.__sub_topping()
		self.dressings = self.__dressings()
		self.en2ko_translator = self.__translator()
		self.ko2en_translator = dict((v,k) for k,v in self.en2ko_translator.items())

	def show_main_toppings(self):
		menu_str = "| "
		item_index = 0
		for item in self.main_toppings.keys():
			menu_str += self.lang_en2ko(item) + ": " + str(self.get_price(item)) + " | "
			item_index += 1
			if (item_index % 3 == 0) and (item_index % 9 != 0):
				menu_str += "\n | "
		return menu_str

	def show_sub_toppings(self):
		menu_str = "| "
		item_index = 0
		for item in self.sub_toppings.keys():
			menu_str += self.lang_en2ko(item) + ": " + str(self.get_price(item)) + " | "
			item_index += 1
			if item_index % 4 == 0:
				menu_str += "\n | "
		return menu_str

	def show_dressings(self):
		menu_str = "| "
		item_index = 0
		for item in self.dressings.keys():
			menu_str += self.lang_en2ko(item) + " | "
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
		return 'not exist price value'

	def get_explain(self, item):
		if item in self.dressings:
			return self.dressings[item]
		return 'not exist explain value'

	def __main_topping(self):
		main_toppings = {
			'chicken':1200,
			'sweet potato':1200,
			'egg':600,
			'tofu':800,
			'bacon':800,
			'ground beef':1000,
			'samon':2000,
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

	def lang_en2ko(self, item):
		if item in self.en2ko_translator:
			return self.en2ko_translator[item]
		return item
	
	def lang_ko2en(self, item):
		if item in self.ko2en_translator:
			return self.ko2en_translator[item]
		return item	
			
	def __translator(self):
		translate = {
			'chicken':u'치킨',
			'sweet potato':u'스윗포테이토',
			'egg':u'에그',
			'tofu':u'두부',
			'bacon':u'베이컨',
			'ground beef':u'그라운드 비프',
			'samon':u'연어',
			'fruit cheese':u'과일치즈',
			'green grapes':u'청포도',
			'cranberry':u'크랜베리',
			'kidney bean':u'강낭콩',
			'corn':u'옥수수',
			'tortilla chip':u'또띠아칩',
			'baked bean':u'베이키드빈',
			'onion':u'양파',
			'shredded cheese':u'쉬레드치즈',
			'nuts':u'견과류',
			'tomato':u'토마토',
			'olve':u'올리브',
			'caesar': u'시저',
			'honey mustard': u"허니머스터드",
			'oriental': u"오리엔탈",
			'creamy chilly': u"크리미칠리",
			'lemon': u"레몬",
			'balsamic': u"발사믹",
			'citron': u"유자",
			'basil pesto': u"바질페스토",
			'size_up': u"사이즈업"
		}
		return translate
	
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
