from django.urls import path
from .views import *


app_name = 'bot'

urlpatterns = [
	path('', index)
]