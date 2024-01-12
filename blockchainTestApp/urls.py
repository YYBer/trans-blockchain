from django.urls import path
from .views import add_game_data

urlpatterns = [
	path('blockchainTest/', add_game_data, name='add_game_data_url'),
]