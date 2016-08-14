from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json

@respond_to('github', re.IGNORECASE)
def github(message):
	attachments = [{
		"fallback": "New ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
		"pretext": "New ticket from Andrea Lee",
		"title": "Ticket #1943: Can't reset my password",
		"title_link": "https://groove.hq/path/to/ticket/1943",
		"text": "Help! I tried to reset my password but nothing happened!",
		"color": "#7CD197"																			}]
	message.send_webapi('hoho', json.dumps(attachments))

@respond_to('hi', re.IGNORECASE)
def hi(message):
	message.reply('I can understand hi or HI!')
	# react with thumb up emoji
	message.react('+1')

@respond_to('I love you')
def love(message):
	message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
	# Message is replied to the sender (prefixed with @user)
	message.reply('Yes, I can!')

	# Message is sent on the channel
	# message.send('I can help everybody!')
