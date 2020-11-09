from django.http import HttpResponse
import json
from telebot import TeleBot


def index(request):
	if request.method == 'POST':
		update = json.loads(request.data)
		bot = TeleBot('1352904574:AAH2gzRkdyrGeufTrgJlBAfk7n1b7PBJ_Es')
		bot.send_message(
			update['message']['from']['id'],
			'<pre>'+str(json.dumps(update, indent=4))+'</pre>',
			parse_mode="HTML")
	return HttpResponse('ok')