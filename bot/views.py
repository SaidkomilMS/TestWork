from django.http import HttpResponse
import json
from telebot import TeleBot

from .models import TGUser


def index(request):
	if request.method == 'POST':
		update = json.loads(request.POST)
		chat_id = update['message']['from']['id']
		text = update['message']['text']
		user, new = TGUser.objects.get_or_create(user_id=chat_id)
		if new:
			user.save()
		bot = TeleBot('1352904574:AAH2gzRkdyrGeufTrgJlBAfk7n1b7PBJ_Es')
		if text != '/start':
			bot.send_message(
				chat_id,
				'<pre>'+str(json.dumps(update, indent=4))+'</pre>',
				parse_mode="HTML"
			)
		else:
			bot.send_message(
				chat_id,
				"Привет!"
			)
	return HttpResponse('ok')