# -*- coding: euc-kr -*- 

class SaladyTranslator(object):

	def __init__(self):
		self.en2ko_translator = self.__translator()
		self.ko2en_translator = dict((v,k) for k,v in self.en2ko_translator.items())

	def __translator(self):
		translate = {
			'chicken':u'ġŲ',
			'sweet potato':u'������������',
			'egg':u'����',
			'tofu':u'�κ�',
			'bacon':u'������',
			'ground beef':u'�׶������',
			'salmon':u'����',
			'fruit cheese':u'����ġ��',
			'green grapes':u'û����',
			'cranberry':u'ũ������',
			'kidney bean':u'������',
			'corn':u'������',
			'tortilla chip':u'�Ƕ��Ĩ',
			'baked bean':u'����Ű���',
			'onion':u'����',
			'shredded cheese':u'������ġ��',
			'nuts':u'�߰���',
			'tomato':u'�丶��',
			'olve':u'�ø���',
			'caesar': u'����',
			'honey mustard': u"��ϸӽ�Ÿ��",
			'oriental': u"������Ż",
			'creamy chilly': u"ũ����ĥ��",
			'lemon': u"����",
			'balsamic': u"�߻��",
			'citron': u"����",
			'basil pesto': u"�����佺��",
			'black sesame': u"������",
			'sour cream': u"����ũ��",
			'parmesan cheese': u"�ĸ���ġ��",
			'size_up': u"�������",
			'sweet':u"����",
			'mexican': u"�ƽ�ĭ",
			'triple cheese': u"Ʈ����ġ��",
			'classic': u"Ŭ����",
			'my': u"����"
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
