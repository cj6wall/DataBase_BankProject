from django.urls import path

from . import views

urlpatterns = [
	path('index/', views.index, name = 'index'),
	path('sign/', views.sign, name='sign'),
	path('bank/', views.bank, name='bank')
]