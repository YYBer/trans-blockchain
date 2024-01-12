from django.urls import path
from .views import add_game_data

app_name = 'blockchainTest'

urlpatterns = [
    path('blockchainTest/', add_game_data, name='add_game_data_url'),
	# path('blockchainTest/<str:p1n>/<int:p1s>/<str:p2n>/<int:p2s>/', add_game_data, name='add_game_data_url'),
]