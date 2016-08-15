#coding: UTF-8

import os

API_TOKEN = os.environ["SLACK_BOT_TOKEN"]
DEFAULT_REPLY = "죄송해요. 아직은 제가 좀 멍청해서 무슨 말인지 모르겠어요."
ERRORS_TO = 'bot_test'

PLUGINS = [
	'basic_plugin',
	'salady_plugin'
]
