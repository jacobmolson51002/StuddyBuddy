from django.urls import path
from . import main

urlpatterns = [
	path('', main.hello, name='main'),
	path('searchQuestion', main.searchQuestion, name='searchQuestion'),
]