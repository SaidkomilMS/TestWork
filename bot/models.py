from django.db import models


class TGUser(models.Model):
	user_id = models.BigIntegerField(verbose_name='Telegram ID', blank=False, null=False)
	started_date = models.DateField(auto_now_add=True, verbose_name="User started bot at")

	class Meta:
		ordering = ('-started_date',)