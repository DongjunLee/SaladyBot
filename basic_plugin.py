#coding: UTF-8

import re
import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to(r'안녕')
def hi(message):
	message.reply('안녕하세요! 저는 Kino라고 해요.')
	# react with thumb up emoji
	message.react('+1')

@respond_to(r'Kino 뜻')
def help(message):
	# Message is sent on the channel
	message.send('Kino는 하와이어로 신체를 뜻해요. 제가 여러분 대신 몸으로 뛰겠다는 뜻이죠!')


