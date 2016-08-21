#coding: UTF-8

import re
import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to(r'안녕')
def hi(message):
	message.reply('안녕하세요! 저는 여러분의 주문을 도와드릴 Salady Bot이에요.')
	# react with thumb up emoji
	message.react('+1')


