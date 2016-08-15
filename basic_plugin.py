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

@listen_to(r'키노')
def help(message):
	# Message is sent on the channel
	message.send('저를 찾으셨나요?')
