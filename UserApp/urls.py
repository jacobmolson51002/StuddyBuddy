from django.urls import path
from . import main
from . import login

urlpatterns = [
	path('', main.hello, name='main'),
	path('search', main.search, name='search'),
    path('question/<str:questionID>/', main.question, name='question'),
	path('login', main.login, name='login')
]