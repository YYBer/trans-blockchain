from django.urls import path
# from .views import add_game_data
# from .views import add_hash_data
from . import views
# from blockchainTestApp.views import add_hash_data_test

urlpatterns = [
	# path('blockchainTest/<str:p1n>/<int:p1s>/<str:p2n>/<int:p2s>/', add_game_data, name='add_game_data_url'),
    path("", views.add_hash_data_test, name='add_hash_data_test'),
    # path('blockchainTest/<str:p1n>/<int:p1s>/<str:p2n>/<int:p2s>/', add_hash_data, name='add_hash_data_url'),
]