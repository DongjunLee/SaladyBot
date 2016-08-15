#coding: UTF-8

from salady.menu import SaladyMenu

class SaladyOrder(object):

	def __init__(self):
		pass

	def order(self, item_list):
		menu = SaladyMenu()

		main_topping = []
		sub_topping = []
		dressing = []
		size_up = False

		for item in item_list:
			item = menu.lang_ko2en(item.strip())
			category = menu.item_2_category(item)
			if category == "main":
				main_topping.append(item)
			elif category == "sub":
				sub_topping.append(item)
			elif category == "dressing":
				dressing.append(item)
			elif category == "size_up":
				size_up = True

		order_preview = ("Main: " + str(main_topping) + " Sub: " + str(sub_topping) + 
						 " dressing: " + str(dressing) + " Size Up: " + str(size_up))
		return order_preview
