# -*- coding: euc-kr -*- 

class SaladyTranslator(object):

	def __init__(self):
		self.en2ko_translator = self.__translator()
		self.ko2en_translator = dict((v,k) for k,v in self.en2ko_translator.items())

	def __translator(self):
		translate = {
			'chicken':u'치킨',
			'sweet potato':u'스윗포테이토',
			'egg':u'에그',
			'tofu':u'두부',
			'bacon':u'베이컨',
			'ground beef':u'그라운드비프',
			'salmon':u'연어',
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
			'honey mustard': u"허니머스타드",
			'oriental': u"오리엔탈",
			'creamy chilly': u"크리미칠리",
			'lemon': u"레몬",
			'balsamic': u"발사믹",
			'citron': u"유자",
			'basil pesto': u"바질페스토",
			'black sesame': u"흑임자",
			'sour cream': u"샤워크림",
			'parmesan cheese': u"파마산치즈",
			'size_up': u"사이즈업",
			'sweet':u"스윗",
			'mexican': u"맥시칸",
			'triple cheese': u"트리플치즈",
			'classic': u"클래식",
			'my': u"마이"
		}
		return translate
	
	def lang_en2ko(self, item):
		if item in self.en2ko_translator:
			return self.en2ko_translator[item]
		return item
	
	def lang_ko2en(self, item):
		if item in self.ko2en_translator:
			return self.ko2en_translator[item]
		return item	
